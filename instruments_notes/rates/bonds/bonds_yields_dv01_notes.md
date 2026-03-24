## **bonds / yields / dv01 notes**

### **bond price vs yield**

bond prices and yields move in opposite directions  
rates ↑ → bond price ↓  
rates ↓ → bond price ↑  

reason → when market yields rise existing bonds paying lower coupons become less attractive so their price must fall  


### **bond pricing**

bond price = present value of future cash flows  

price = sum of discounted coupons + discounted face value  

example  
price = C/(1+y) + C/(1+y)^2 + ... + (C+F)/(1+y)^n  


### **duration intuition**

duration measures how sensitive a bond price is to changes in interest rates  

higher duration → larger price move for the same rate change  

longer maturity bonds usually have higher duration → therefore they move more when rates change  

low coupon bonds also have higher duration  


### **duration vs dv01**

duration = percentage sensitivity  
dv01 = dollar sensitivity  

duration tells you relative risk  
dv01 tells you actual p&l impact  


### **dv01 definition**

dv01 = dollar value of a 1 basis point move in yields  

it measures how much the price of a bond or portfolio changes if rates move by 1bp  


### **dv01 calculation**

dv01 ≈ duration × price × 0.0001  

higher duration or higher price → higher dv01 → higher rate risk  


### **dv01 intuition**

if dv01 = 7000  
rates ↑ 1bp → portfolio loses $7000  
rates ↓ 1bp → portfolio gains $7000  

example  
dv01 = 7000  
rates move = 5bp  
p&l = 7000 × 5 = 35000  


### **p&l rule**

long bonds → lose when rates rise  
short bonds → gain when rates rise  

dv01 > 0 → long bonds  
dv01 < 0 → short bonds  


### **portfolio dv01**

dv01 is additive across positions  

total dv01 = sum of individual dv01s  

example  
bond A dv01 = 4000  
bond B dv01 = 3000  
portfolio dv01 = 7000  


### **hedging intuition**

interest rate risk is managed by offsetting dv01  

example  
portfolio dv01 = +7000  

to hedge → take position with dv01 = −7000  

result → net dv01 = 0  


### **yield curve intuition**

front end of the curve reflects central bank expectations  

long end of the curve reflects growth and inflation expectations  

memory trick  
front end → central bank policy  
long end → growth and inflation  


### **curve moves**

bear move → yields rising  
bull move → yields falling  

steepening → long yields move more  
flattening → short yields move more  


### **examples**

bear steepening → yields rise and long-term yields rise more → inflation expectations  

bear flattening → yields rise and short-term yields rise more → central bank tightening  

bull steepening → yields fall and long-term yields fall more → recession fears  

bull flattening → yields fall and short-term yields fall more → central bank cutting rates  


### **forward rate intuition**

forward rates represent the interest rate implied today for a future period  

if long maturity yields > short maturity yields → market expects future rates to rise  

if long maturity yields < short maturity yields → market expects future rates to fall  


### **policy sensitivity**

the 2-year treasury yield reacts most directly to central bank expectations  

because it reflects the expected path of policy rates  


### **convexity intuition**

duration assumes a linear relationship between bond price and yield  

in reality the relationship is curved (convex)  

→ bonds gain more when yields fall  
→ bonds lose less when yields rise  

convexity becomes important for large rate moves  