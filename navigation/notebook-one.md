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

<script>

%%javascript

let list = [1,2,3,4,5];

<script>

When we refer to an element in our array, we start with list[0]. In this case, list[0] = 1. List[1] = 2, list[2] = 3, etc.

We can output any element from our list using the console.log function.

ex: 

<script>

%%javascript

let list2 = [1,2,3,4,5];

console.log(list2[0]); //this prints 1 as it is the first element in the array.
console.log(list2[1]); //this prints 2
console.log(list2[2]); //this prints 3
console.log(list2[3]); //this prints 4
console.log(list2[4]); //this prints 5 

<script>

To delete one of the elements, we can use the pop(index) function or the splice() function. The pop function deletes the last element in a list, while splice deletes an element of your choosing. The formatting for each is below.

<script>

%%javascript

let list3 = [1,2,3,4,5];

list3.pop(); //this deletes the last value in the list.

list3.splice(3, 1); //The 3 indicates that you're deleting the 4th element, which is 4. The 1 tells how many elements you are deleting from that index, so since it's 1, we're just deleting the 4th element.

<script>

We can add and assign values to elements in an array. We use this command to change values

<script>

%%javascript

let list4 = [1,2,3,4,5];

list4[2]=6; //this changes the element in the 2nd position' value from 3 to 6

console.log(list4);

<script>

We use this command to add values:

<script>

let list5=[]; //creates the blank list

list5.push(1);
list5.push(2);
list5.push(3);

//this adds the elements 1,2, and 3 to the list

<script>