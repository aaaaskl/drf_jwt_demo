from django.test import TestCase

import time
import jwt
import datetime
import json, base64
from calendar import timegm





# jwt_token = jwt.encode(token_dict,  # payload, 有效载体
#                        "zhananbudanchou1234678",  # 进行加密签名的密钥
#                        algorithm="HS256",  # 指明签名算法方式, 默认也是HS256
#                        headers=headers  # json web token 数据结构包含两部分, payload(有效载体), headers(标头)
#                        )  # python3 编码后得到 bytes, 再进行解码(指明解码的格式), 得到一个str
#
# print(jwt_token)






def encrypt(ori):
	data_encrypted = base64.b64encode(json.dumps(ori).encode()).decode()
	return data_encrypted

import hashlib
def signature_encrypted(data,salt='sunlei123'):
	hash256 = hashlib.sha256()
	hash256.update(data.encode('utf-8'))
	hash256.update(salt.encode('utf-8'))
	return hash256.hexdigest()



if __name__ == '__main__':

	# datetime -->  time.struct_time(时间元组)
	# datetime.timetuple() 得到一个 时间元组
	# from calendar import timegm
	# timegm(时间元组) --> 时间戳


	# print(exp_time,type(exp_time))
	# print(exp_time.timetuple())
	# print(timegm(exp_time.timetuple()))


	exp_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
	timestamp = timegm(exp_time.timetuple())

	headers = {
		"alg": "HS256",
		"typ": "JWT"
	}

	payload = {
		'user_id': 110,  # 自定义用户ID
		'username': 'sunlei',  # 自定义用户名
		'exp': timestamp  # 超时时间
	}
	header_encrypted = encrypt(headers)
	payload_encrypted = encrypt(payload)
	signature = header_encrypted+'.'+payload_encrypted
	print(signature)
	s = signature_encrypted(signature)
	print(s)