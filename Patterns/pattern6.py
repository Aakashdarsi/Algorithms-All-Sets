'''      * 
        * * 
       * * * 
      * * * * 
     * * * * * 
    * * * * * * 
   * * * * * * * 
  * * * * * * * * 
 * * * * * * * * * 
* * * * * * * * * * 
 * * * * * * * * * 
  * * * * * * * * 
   * * * * * * * 
    * * * * * * 
     * * * * * 
      * * * * 
       * * * 
        * * 
         * 

'''
n = int(input())
total_rows=2*n 
for i in range(1,total_rows):
    if i<=n:
        no_of_spaces = " "*(n-i)
        no_of_stars = "* "*i 
        print(no_of_spaces+no_of_stars)
    else:
        no_of_spaces = " "*(i-n)
        no_of_stars = "* "*(total_rows-i)
        print(no_of_spaces+no_of_stars)