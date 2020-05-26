##############################################################################
# Copyright 2020 IBM Corp. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
##############################################################################
CKM_RSA_PKCS_KEY_PAIR_GEN = 0x00000000
CKM_MD5_RSA_PKCS          = 0x00000005
CKM_SHA256_RSA_PKCS       = 0x00000040

CKM_ECDSA_SHA1            = 0x00001042
CKM_EC_KEY_PAIR_GEN       = 0x00001040

CKM_AES_KEY_GEN        = 0x00001080
CKM_AES_CBC            = 0x00001082
CKM_AES_CBC_PAD        = 0x00001085

CKA_CLASS              = 0x00000000
CKA_TOKEN              = 0x00000001
CKA_PRIVATE            = 0x00000002
CKA_LABEL              = 0x00000003
CKA_APPLICATION        = 0x00000010
CKA_VALUE              = 0x00000011
CKA_OBJECT_ID          = 0x00000012
CKA_CERTIFICATE_TYPE   = 0x00000080
CKA_ISSUER             = 0x00000081
CKA_SERIAL_NUMBER      = 0x00000082
CKA_AC_ISSUER          = 0x00000083
CKA_OWNER              = 0x00000084
CKA_ATTR_TYPES         = 0x00000085
CKA_TRUSTED            = 0x00000086
CKA_CERTIFICATE_CATEGORY        = 0x00000087
CKA_JAVA_MIDP_SECURITY_DOMAIN   = 0x00000088
CKA_URL                         = 0x00000089
CKA_HASH_OF_SUBJECT_PUBLIC_KEY  = 0x0000008A
CKA_HASH_OF_ISSUER_PUBLIC_KEY   = 0x0000008B
CKA_NAME_HASH_ALGORITHM         = 0x0000008C
CKA_CHECK_VALUE                 = 0x00000090

CKA_KEY_TYPE           = 0x00000100
CKA_SUBJECT            = 0x00000101
CKA_ID                 = 0x00000102
CKA_SENSITIVE          = 0x00000103
CKA_ENCRYPT            = 0x00000104
CKA_DECRYPT            = 0x00000105
CKA_WRAP               = 0x00000106
CKA_UNWRAP             = 0x00000107
CKA_SIGN               = 0x00000108
CKA_SIGN_RECOVER       = 0x00000109
CKA_VERIFY             = 0x0000010A
CKA_VERIFY_RECOVER     = 0x0000010B
CKA_DERIVE             = 0x0000010C
CKA_START_DATE         = 0x00000110
CKA_END_DATE           = 0x00000111
CKA_MODULUS            = 0x00000120
CKA_MODULUS_BITS       = 0x00000121
CKA_PUBLIC_EXPONENT    = 0x00000122
CKA_PRIVATE_EXPONENT   = 0x00000123
CKA_PRIME_1            = 0x00000124
CKA_PRIME_2            = 0x00000125
CKA_EXPONENT_1         = 0x00000126
CKA_EXPONENT_2         = 0x00000127
CKA_COEFFICIENT        = 0x00000128
CKA_PUBLIC_KEY_INFO    = 0x00000129
CKA_PRIME              = 0x00000130
CKA_SUBPRIME           = 0x00000131
CKA_BASE               = 0x00000132
CKA_PRIME_BITS         = 0x00000133
CKA_SUBPRIME_BITS      = 0x00000134
CKA_SUB_PRIME_BITS     = CKA_SUBPRIME_BITS
CKA_VALUE_BITS         = 0x00000160
CKA_VALUE_LEN          = 0x00000161
CKA_EXTRACTABLE        = 0x00000162
CKA_LOCAL              = 0x00000163
CKA_NEVER_EXTRACTABLE  = 0x00000164
CKA_ALWAYS_SENSITIVE   = 0x00000165
CKA_KEY_GEN_MECHANISM  = 0x00000166

CKM_SHA_1              = 0x00000220


# CKA_VALUE_LEN
# CKA_WRAP
# CKA_UNWRAP
# CKA_ENCRYPT
# CKA_DECRYPT,
# CKA_EXTRACTABLE
# CKA_TOKEN

CKR_OK                 = 0x00000000

AES_BLOCK_SIZE         = 16

