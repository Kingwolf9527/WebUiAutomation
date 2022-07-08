# -*- coding: utf-8 -*-
#   @Author    :    KingWolf
#   @Time      :    2022/6/24 6:57
#   @File      :    common_encryptions.py
#   @Project   :    WebUiAutomation

import os
from hashlib import sha256
from hmac import HMAC


class CommonEncryption(object):

    def encrypt_password(self, password, salt=None):
        """
        Hash password on the fly.
        @param password:
        @param salt:
        @return:
        """
        if salt is None:
            salt = os.urandom(8)     # 64 bits.
        
        assert 8 == len(salt)
        assert isinstance(salt, bytes)
        
        if isinstance(password, str):
            password = password.encode("UTF-8")

        assert isinstance(password, bytes)

        result = password
        for i in range(10):
            result = HMAC(result, salt, sha256).digest()
            
        return salt + result

    def validate_password(self, hashed, input_password):
        return hashed == self.encrypt_password(input_password, salt=hashed[:8])
        


if __name__ == '__main__':
    password = '123456'
    haseed = CommonEncryption().encrypt_password(password)
    assert CommonEncryption().validate_password(haseed, password)
    print(haseed)

    
