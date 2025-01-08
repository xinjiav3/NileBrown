---
layout: page
title: Notebook One
permalink: /nb1/
---

Hi there!
<br>
Today, we'll be teaching you all about arrays!!

Arrays are variables that store a list of elements. In our example, we will have the list of the numbers 1-5.

We create it like so:

%%js

let list = [1,2,3,4,5];

When we refer to an element in our array, we start with list[0]. In this case, list[0] = 1. List[1] = 2, list[2] = 3, etc.

We can output any element from our list using the console.log function.

ex: 

%%js

let list = [1,2,3,4,5];

console.log(list[0]); //this prints 1 as it is the first element in the array.
console.log(list[1]); //this prints 2
console.log(list[2]); //this prints 3
console.log(list[3]); //this prints 4
console.log(list[4]); //this prints 5 

To delete one of the elements, we can use the pop(index) function or the splice() function. The pop function deletes the last element in a list, while splice deletes an element of your choosing. The formatting for each is below.

%%js

let list = [1,2,3,4,5];

list.pop(); //this deletes the last value in the list.

list.splice(2, 1);

