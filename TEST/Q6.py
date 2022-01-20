#ref
orders={'dabeli':'30','vadapav':'25','sevpuri':'35','dahipuri':'45'}
sort_orders=sorted(orders.items(),key=lambda x: x[1],reverse=True)
for i in sort_orders:
    print(i[0],i[1])