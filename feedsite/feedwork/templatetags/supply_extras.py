from django import template

register = template.Library()

@register.filter

def work_on_amount(value,args):
	print(args)
	# since we can be able to grab the query object this side , then we can use it the way we want too

	# the amount by multiplying the unit_price and the quantity
	amount = args.unit_price * args.quantity

	return amount

@register.filter
def work_on_the_full_amount(value,args):
	#first thing is to get the amount
	amount = args.unit_price * args.quantity


	#is equal to amount + transport + onloading + offloading + grinding
	fullamount = amount + args.transport + args.onloading + args.offloading + args.grinding


	return fullamount

@register.simple_tag
def multiple_ops(loading,off_loading,transport,quantity,unit_price):
   #do your stuff
   cost_of_purchase = (loading+off_loading+transport)+(quantity*unit_price)
   return cost_of_purchase
