import sys
sys.path.append("../")

import pytest
import os
from payments.pix import Pix

def test_pix_create_payment():
    pix_instance = Pix()

    #create_a_payment
    payment_info = pix_instance.create_payment(base_dir="../")

    print(payment_info)