# js:
# function solution(number){
# console.log(number)
#   if (number < 0) {
#     return 0
#   }
#  let arr = []
#   for (let i = 1; i < number; i++) {
#     if (i % 15 === 0) {
#       arr.push(i)
#     } else if (i % 5 === 0) {
#       arr.push(i)
#     } else if (i % 3 === 0) {
#       arr.push(i)
#     }
#   }
#   if (arr.length !== 0) {
#   return arr.reduce((a, b) => a+b)

# }
# return 0
# }


def solution(number):
    if number < 0:
        return 0
    result = []
    print(number)
    for i in range(1, number):
        if i % 5 == 0:
            result.append(i)
        elif i % 3 == 0:
            result.append(i)
    if len(result) != 0:
        return sum(result)
    return 0
