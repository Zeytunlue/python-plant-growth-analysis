#creating the data
growth = [3, 1, 2, 4, 2, 3, 2]
#sorting the list
growth.sort()
#finding the smallest and biggest growth numbers in the list
smallest_growth = growth[0]
print(f'The smallest growth in the week is: {smallest_growth}cm')
biggest_growth = growth[6]
print(f'The biggest growth in the week is: {biggest_growth}cm')
#finding the average growth in the list
average_growth = sum(growth) / len(growth)
average_growth = round(average_growth, 2)
print(f'The average growth in the week is: {average_growth}cm')
#adding another list
new_growth = [2, 0, 3, 2, 4, 5, 4]
#joining the two lists
joined_growth = growth + new_growth
#finding the smallest and biggest growth numbers in the joined list
joined_smallest_growth = min(joined_growth)
print(f'The smallest growth in these 2 weeks is: {joined_smallest_growth}cm')
joined_biggest_growth = max(joined_growth)
print(f'The biggest growth in these 2 weeks is: {joined_biggest_growth}cm')
#finding the average growth in the joined list
joined_average_growth = sum(joined_growth) / len(joined_growth)
joined_average_growth = round(joined_average_growth, 2)

print(f'The average growth in these 2 weeks is: {joined_average_growth}cm')
joined_smallest_growth_count = joined_growth.count(joined_smallest_growth)
print(f'The smallest growth happened {joined_smallest_growth_count} times in these 2 weeks')
joined_biggest_growth_count = joined_growth.count(joined_biggest_growth)
print(f'The biggest growth happened {joined_biggest_growth_count} times in these 2 weeks')