from bech32 import bech32_decode, bech32_encode, convertbits, decode

from terra_sdk.core.bech32 import get_bech
from terra_sdk.core.public_key import SimplePublicKey, address_from_public_key


def acc_to_public(acc_address: str) -> SimplePublicKey:
    data = decode("terra", acc_address)
    # hex = convertbits(data, 5, 8)
    return SimplePublicKey(bytes.fromhex(data))


def public_to_acc(public_key: SimplePublicKey) -> str:
    raw_address = address_from_public_key(public_key)
    return get_bech("terra", raw_address.hex())


def get_bech(prefix: str, payload: str) -> str:
    data = convertbits(bytes.fromhex(payload), 8, 5)
    if data is None:
        raise ValueError(f"could not parse data: prefix {prefix}, payload {payload}")
    return bech32_encode(prefix, data)  # base64 -> base32
