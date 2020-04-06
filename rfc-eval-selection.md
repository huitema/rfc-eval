In order to avoid injecting personal bias in the random selection, we use
a random selection process similar to the Nomination Committee selection
process defined in {{?RFC3797}}. The process is seeded with the text string
"vanitas vanitatum et omnia vanitas", and the results are:

~~~ 
Picking 20 numbers between 8307 and 8511,
using MD5(vanitas vanitatum et omnia vanitas)
Rank 1: 8411 -- md5=daba041224a879199b698748808f917d
Rank 2: 8456 -- md5=f5570484d91ada6a672edbdca61d808c
Rank 3: 8446 -- md5=8340e918bb8faf69d197f79c9a58d7b8
Rank 4: 8355 -- md5=19474df74efd9917cf3fe8acce2ac374
Rank 5: 8441 -- md5=5acce2b730f3c24a4a91a5fc1921d1cd
Rank 6: 8324 -- md5=411c11a1cf4c292f83458865599c6921
Rank 7: 8377 -- md5=ac16a89192c0f0727febd35aacbc1f24
Rank 8: 8498 -- md5=bba44f2ba1ab240a1265a82ab71f7e02
Rank 9: 8479 -- md5=1653606b0af95d529a473a8f85ffaea4
Rank 10: 8453 -- md5=0cbfe105667c5a83b027dcfa85062f98
Rank 11: 8429 -- md5=fa51d7738562d990926a0d199fb060b8
Rank 12: 8312 -- md5=96d061523b1a57343356ae7a1e498ca5
Rank 13: 8492 -- md5=1b72b746eb05f79af40ed2bd3faccbe8
Rank 14: 8378 -- md5=645833b936d36cdcc797256518d7c483
Rank 15: 8361 -- md5=2064622c868e410beb0d9c18d0cb522c
Rank 16: 8472 -- md5=ca8a823072a21df011d0ea8b96a6aa47
Rank 17: 8471 -- md5=01b293a7dd0793e6f3297f2a973cd7e3
Rank 18: 8466 -- md5=8e411babe271557fe83bcdececc1643f
Rank 19: 8362 -- md5=8a1ba3efd82856a12b2b35fc5237e1b7
Rank 20: 8468 -- md5=57ae50ee0e1e0708d356d96d116dbfe1
~~~


When evaluating delays and impact, we will compare the year 2018 to 2008 and
1998, 10 and 20 years ago. To drive this comparison, we pick 20 RFC at random
among those published in 2008, and another 20 among those published in 1998.
We use the same nomcom-like methodology.

For 2008, we picking random RFC numbers between RFC 5134
(January 2008) and RFC 5405 (December 2008), using the sentence "sed fugit interea
fugit irreparabile tempus" as a seed. We actually list here 21 numbers, because
the random draw place RFC 5315 in 20th position, but that RFC was never issued.
We replace it by RFC 5301, which came in 21st position.

~~~
Picking 21 numbers between 5134 and 5405,
using MD5(sed fugit interea fugit irreparabile tempus)
Rank 1: 5227 -- md5=61e5b3cd97fda4e75450e93df0744b6d
Rank 2: 5174 -- md5=eed49542394e9d392bcd756ee0f5beed
Rank 3: 5172 -- md5=72055ca953d6a8ee0d60a9fca0b8d738
Rank 4: 5354 -- md5=7a00ef15897479d1d15255159f6d8674
Rank 5: 5195 -- md5=54813be7bb56f48a05af8c894799b51f
Rank 6: 5236 -- md5=153263bbd8c0349501b75a33f3d66f6c
Rank 7: 5348 -- md5=b2d19aa9c1250ef2ddf169045f6e99d7
Rank 8: 5281 -- md5=1c3e61643d46d1da4ba16f0fd7a0aff5
Rank 9: 5186 -- md5=5e87001b830183b1a9427d479a7b0e42
Rank 10: 5326 -- md5=024347839f83d8082549c08bdfa1b43e
Rank 11: 5277 -- md5=049a83016ab08552841c59400480cd9d
Rank 12: 5373 -- md5=a1ce374aaebdacca2e7d6eeff039d970
Rank 13: 5404 -- md5=fb0d6b582a27ce34175e39de33598556
Rank 14: 5329 -- md5=df043ef1f9d42ba12a03a84434d26ead
Rank 15: 5283 -- md5=c40d3f966bc7800d6508d3d82df2371d
Rank 16: 5358 -- md5=6fea5bdb26b19e68befd409a09cb335d
Rank 17: 5142 -- md5=a8844b73287781762e6548fc6f533508
Rank 18: 5271 -- md5=c19eb02984265ecfe4ca076f2c160cfa
Rank 19: 5349 -- md5=33d756f81bf6e40ff344cf6ccaf29f13
Rank 20: 5315 -- md5=d4c30875f88328d72c9f78def2d1dde5
Rank 21: 5301 -- md5=3356419e5560901f0d31309b39d14a80
~~~

For 1998 we picking random RFC numbers between RFC 2257
(January 1998) and RFC 2479 (December 1998), using the sentence
"pulvis et umbra sumus" as a seed.

~~~
Picking 20 numbers between 2257 and 2479,
using MD5(pulvis et umbra sumus)
Rank 1: 2431 -- md5=6eba444bb3349339fcde7e2be726f0f0
Rank 2: 2381 -- md5=0ce53f69f1a49a49309054af1e9a1d42
Rank 3: 2387 -- md5=53726e77ffeed903d244155d28e30f10
Rank 4: 2348 -- md5=69fcab2d2085555bac9eb0e0f4346523
Rank 5: 2391 -- md5=93358a26a7fce9fa9d61a31cdfdb87b7
Rank 6: 2267 -- md5=652dcab91bd9d5c58f98bdab21b23d80
Rank 7: 2312 -- md5=2505b0bed4af0a00ee663891c6f294d8
Rank 8: 2448 -- md5=6ede4b0dfa935f6ca656a5104b8dc5d0
Rank 9: 2374 -- md5=5312bfe5a9ca45563eb0bf35510d8daa
Rank 10: 2398 -- md5=7748a6deec3860898678f992b0b22792
Rank 11: 2283 -- md5=d73ff67466eb42d971a0e134b9284f83
Rank 12: 2382 -- md5=de1f667ac3e4c64aa529872e08823dff
Rank 13: 2289 -- md5=37773c2569dc25fdd0ab400ea401d5c7
Rank 14: 2282 -- md5=6b3df671a0a0becf9e42d203b59acd08
Rank 15: 2404 -- md5=e1b6819e5355924f456eb79f93beb8fd
Rank 16: 2449 -- md5=4f057df7c226efea773e7013c9c62081
Rank 17: 2317 -- md5=40eee3b536abe4afdb8834a0650c0a04
Rank 18: 2394 -- md5=044f09c53fc9fd1c50fe6bd0c39318e1
Rank 19: 2297 -- md5=78ee7e128436c969c80900fef80c075c
Rank 20: 2323 -- md5=ea6935bbda5f6d97756d3df5c3e2fdfb
~~~
