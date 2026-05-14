def second_largest_distinct(nums):
    #here first and second is none
    first = second = None
    #for using the n value in nums to check it is frist then move to second here delcare continue
    for n in nums:
        if n == first or n == second:
            continue
        if first is None or n > first:
            second = first
            first = n
        elif (second is None or n > second):
            second = n
    return second if second is not None else -1