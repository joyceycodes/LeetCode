// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.

var isValid = function(s) {
    let stack = []
    let hashmap = {
        '}' : '{',
        ')' : '(',
        ']' : '[',
    }

    for(let i = 0; i<s.length; i++){
        if (s[i] in hashmap){
            if(stack && stack[stack.length-1] === hashmap[s[i]]){
                stack.pop()
            } else{
                return false
            }
        } else{
            stack.push(s[i])
        }
    }

    return stack.length === 0 ? true : false
};