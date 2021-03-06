cost_hash ={
"57247":"0.0887",
"98732":"0.1856",
"134928":"0.2307",
"77275":"0.1522",
"29240":"0.0532",
"15440":"0.0250",
"70820":"0.1409",
"139603":"0.2541",
"63718":"0.1147",
"143807":"0.2660",
"190457":"0.2933",
"40572":"0.0686"
}

new_hash = []
max_byte_size = 0
sumt = 0
for byte_size, fee in cost_hash.items():
	new_hash.append({"byte_size": int(byte_size), "fee": float(fee), "avg": float(fee)/int(byte_size)})
newlist = sorted(new_hash, key=lambda k: k['avg'], reverse=True)
index = 0
fee_count = 0
while(max_byte_size < 1000000 and index < len(newlist)):
	max_b_size = max_byte_size + newlist[index]['byte_size']
	if max_b_size > 1000000:
		print("{}".format(newlist[index]['byte_size']))
		index += 1
		continue
	fee_count += newlist[index]['fee']
	index +=1
	max_byte_size = max_b_size
fee_count += 12.5
print("max_byte_size={}\n".format(max_byte_size))
print("fee={}\n".format(fee_count))