# > sudo iptables -S
# > sudo python3 cant_touch_this.py

# 1. and 2. can be executed all together or one by one with 'sudo iptables -S' command in between


# The below code can recreate one of the below commands to iptables
# > iptables -A INPUT -p tcp --dport 443 -j DROP
# > iptables -A INPUT -p tcp --dport 443 -j REJECT


# # Main part, always needed:
import iptc
table = iptc.Table(iptc.Table.FILTER)


# 1. Stops HTTPS traffic (by adding rule in iptables to reject/ drop input on port 443):
rule = iptc.Rule()
rule.protocol = 'tcp'
rule.src = 'x.x.x.x/255.255.255.255' #To be adjusted

match = iptc.Match(rule, 'tcp')
match.dport = '443' #HTPPS traffic
rule.add_match(match)

rule.target = iptc.Target(rule, 'DROP') # REJECT also possible

chain = iptc.Chain(table, 'INPUT') #INPUT or OUTPUT
chain.insert_rule(rule)
table.refresh()
# 1. end

# Walking around the iptables from python, might be useful:
for chain in table.chains:
	# print(chain.__dir__())
	for rule in chain.rules:
		# print(rule.__dir__())
		print(rule.src)
		# print(rule.entry.__dir__())
		print(rule.target.name)
		print(rule.protocol)
		for match in rule.matches:
			# print(match.__dir__())
			print(match.parameters['dport'])


# 2. Finds and removes this rule from iptables, Filter table:
for chain in table.chains:
	for r in chain.rules:
		print(r.target.name)
		if r.target.name in ['DROP', 'REJECT'] and \
			r.protocol == 'tcp' and \
			r.matches[0].parameters['dport']:
			chain.delete_rule(r)
			break
		break
table.refresh()
# 2. end