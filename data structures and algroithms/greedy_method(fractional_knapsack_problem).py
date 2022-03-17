class fractional_knapsack_problem:
    def __init__(self, value, weight, capacity):
        self.value = value
        self.weight = weight
        self.capacity = capacity
        self.ratios_bag = {}
        self.sorted_ratios_bag = {}

    def find_ratios(self):
        for i in range(len(self.weight)):
            ratio = self.value[i] / self.weight[i]
            self.ratios_bag[ratio] = {'value': self.value[i], 'weight': self.weight[i]}

        ratios = list(self.ratios_bag.keys())
        ratios.sort(reverse=True)
        for i in ratios:
            self.sorted_ratios_bag[i] = self.ratios_bag[i]
        print(self.sorted_ratios_bag)

    def stealing(self):
        fully = False
        total_weight = 0
        bag = 0
        last_total_weight = 0
        keys = list(self.sorted_ratios_bag.keys())
        keys.sort()
        while not fully:
            thing = self.sorted_ratios_bag.pop(keys.pop())
            thing_weight = thing['weight']
            thing_value = thing['value']
            total_weight += thing_weight
            if total_weight > capacity:
                last_thing = {(last_total_weight/thing_weight)*thing['value']/last_total_weight: {'weight': last_total_weight, 'value': (last_total_weight/thing_weight)*thing['value']}}
                bag += last_thing[(last_total_weight/thing_weight)*thing['value']/last_total_weight]['value']
                last_total_weight += last_thing[(last_total_weight/thing_weight)*thing['value']/last_total_weight]['weight']
                fully = True
                
                pass
            elif total_weight < capacity:
                bag += thing_value
                print(total_weight)
                last_total_weight += thing['weight']
                last_total_weight = capacity - total_weight
                print(f"max number is {bag}")
            elif total_weight == capacity:
                fully = True
        print("max value is ", bag)



value = [120, 100, 60]
weight = [30, 20, 10]
capacity = 50
method = fractional_knapsack_problem(value, weight, capacity)
method.find_ratios()
method.stealing()