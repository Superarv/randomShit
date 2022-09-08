
# Complex Clock App Documentation
### This is a clock app with three main functions: Timer, Stopwatch, and World Clock </h4>
## External Library Guide: 
## First, import the library into your program using whatever you named the file, I'll use 'complexClock':
   
    import complexClock as clock
    
## Timer Function: Counts down from time that is inputted 
    timer(input) 
#### The 'input' parameter should be a sinlge string that is structured: "{minutes}:{seconds}", (ex. 5:01) [SPACING DOES MATTER]
## Stopwatch Function: Counts upwards until program is ended 
    stopwatch() 
#### Function takes no arguments   
## World Time Clock: Returns the local time of given city 
    world_time(input) 
#### The 'input' parameter should be a single string that is structured: "{region}/{city}" or "{timezone}", (ex. America/Chicago or ROC) [SPACING DOES MATTER] 
#### Pay a vist to <a href="https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568">this page</a> to see what the acceptable timezones are
