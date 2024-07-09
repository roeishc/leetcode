class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        order_finish_at = customers[0][0] + customers[0][1]
        total_waiting_times = customers[0][1]

        for arrival, time in customers[1:]:
            if arrival < order_finish_at:
                order_finish_at += time
                total_waiting_times += order_finish_at - arrival
            else:
                order_finish_at = arrival + time
                total_waiting_times += time

        return total_waiting_times / len(customers)


        # initial solution: O(n) time, O(n) space

        # waiting_times = []
        # order_finish_at = customers[0][0] + customers[0][1]
        # waiting_times.append(customers[0][1])

        # for arrival, time in customers[1:]:
        #     if arrival < order_finish_at:
        #         order_finish_at += time
        #         waiting_times.append(order_finish_at - arrival)
        #     else:
        #         order_finish_at = arrival + time
        #         waiting_times.append(time)

        # return sum(waiting_times) / len(waiting_times)
