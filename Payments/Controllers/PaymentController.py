from CustomUsers.models import CustomUser
from Services.models import Service
from ..models import Wallet, Payment
from blockcypher.api import coin_symbol_from_mkey
import blockcypher
import string
import random


class PaymentController:
    wallet = None
    api = 'a2166a1520634142b3be1e17304fe105'
    wallet_name = 'fivvr_wallet_test'
    xpubkey = 'xpub661MyMwAqRbcFtXgS5sYJABqqG9YLmC4Q1Rdap9gSE8NqtwybGhePY2gZ29ESFjqJoCu1Rupje8YtGqsefD265TMg7usUDFdp6W1EGMcet8'

    def gen(self):
        try:
            wallet = Wallet.objects.get(id=1)
            self.get_wallet(wallet)
        except:
            new_wallet = blockcypher.create_hd_wallet(
                wallet_name=self.wallet_name,
                xpubkey=self.xpubkey,
                api_key=self.api,
                coin_symbol=coin_symbol_from_mkey(self.xpubkey)
            )
            wallet = Wallet()
            wallet.create(
                key=new_wallet['extended_public_key'],
                hd=new_wallet['hd'],
                name=new_wallet['name'],
                token=new_wallet['token']
            )
            wallet.save()
            self.wallet = new_wallet

    def get_wallet(self, wallet):
        self.wallet = blockcypher.get_wallet_addresses(wallet_name=wallet.name, api_key=self.api, is_hd_wallet=True)

    def create_address(self):
        chain = blockcypher.derive_hd_address(
            api_key=self.api,
            wallet_name=self.wallet_name,
            coin_symbol=coin_symbol_from_mkey(self.xpubkey)
        )
        address = chain["chains"][0]["chain_addresses"][0]["address"]

        return address

    # Create an payment and add address to this
    def create_payement_for_service(self, request, service_id):
        service = Service.objects.get(id=service_id)

        payment = Payment()
        payment.sender = CustomUser.objects.get(api_key=request.POST.get('api'))
        payment.receiver = service.author
        payment.post = service
        # Onderstaande code had een wallet moeten aanmaken om hiermee de betaling te ontvangen
        # payment.wallet = self.create_address()]
        # Vervangen voor deze random code generatie, dit werkt natuurlijk niet
        letters = string.hexdigits
        payment.wallet = ''.join(random.choice(letters) for i in range(25))
        payment.save()

        service.author.add_karma()

    def service_cancel(self, request, payment_id):
        payment = Payment.objects.get(id=payment_id)
        if payment.sender == CustomUser.objects.get(api_key=request.POST.get('api')):
            payment.status = 'canceled'
            payment.sender.substract_karma()
            payment.sender.substract_karma()
        elif payment.receiver == CustomUser.objects.get(api=request.POST.get('api')):
            payment.status = 'canceled'
            payment.sender.substract_karma()
            payment.sender.substract_karma()

        if payment.status == 'canceled':
            return {
                'status': 'success'
            }
        else:
            return {
                'status': 'failed',
                'reason': 'User is not sender or receiver'
            }

    # Check address for value
    def check_service_payed(self, payment_id):
        payment = Payment.objects.get(id=payment_id)
        payed = blockcypher.get_total_balance(payment.wallet, 'btc')
        if payed == payment.post.cost:
            payment.status = 'payed'
            return {
                'status': 'success'
            }
        else:
            return {
                'status': 'failed',
                'reason': 'not enough has been payed'
            }

    def get_payments_for_service(self, service_id):
        payments = Payment.objects.filter(post=service_id)
        payment_array = []
        for payment in payments:
            payment_array.append(payment.serialize())

        return payment_array
