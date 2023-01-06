// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// Example 1:

// Input: s = "anagram", t = "nagaram"
// Output: true
// Example 2:

// Input: s = "rat", t = "car"
// Output: false
 

// Constraints:

// 1 <= s.length, t.length <= 5 * 104
// s and t consist of lowercase English letters.

var isAnagram = function(s, t) {
    let hashmap = {}
    for(let i = 0; i < s.length; i++){
        if (!(s[i] in hashmap)) {
            hashmap[s[i]] = 0
        } 
        hashmap[s[i]] += 1
    }

    for(let i = 0; i < t.length; i++){
        const re = new RegExp(t[i], 'g')
        const count = t.match(re).length
        if(count !== hashmap[t[i]] || t.length !== s.length){
            return false
        }
    }
    return true
};

// time complexity: O(n)
// space complexity: O(n)