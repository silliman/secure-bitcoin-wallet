#!/bin/bash
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

user=${$1:-}

echo "wallet="$wallet
echo ""
echo "********** REMOVING WALLETS **********"
echo ""
./rm-wallet.sh $user charlie
./rm-wallet.sh $user devil
./rm-wallet.sh $user eddy
echo ""
echo "********** RUNNING WALLETS ***********"
echo ""
./run-wallet.sh $user charlie
./run-wallet.sh $user devil
./run-wallet.sh $user eddy
echo ""
echo "********** URLS **********************"
echo ""
./wallet-url.py $user charlie 
./wallet-url.py $user devil
./wallet-url.py $user eddy
echo ""
echo "********** DONE **********************"
