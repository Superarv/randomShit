<div align = "center">
<h1> Complex Clock App Documentation</h1>
<h4> This is a clock app with three main functions: Timer, Stopwatch, and World Clock </h4>
<h2> External Library Guide: </h2>
  <div align = "left">
  <h2>First, import the library into your program using whatever you named the file, I'll use 'complexClock': 
    <h3>import complexClock as clock</h3>
    <h3></h3>
    <h2>Timer Function: Counts down from time that is inputted</h2>
    <h3>timer(input)</h3>
    <h4>The 'input' parameter should be a sinlge string that is structured: "{minutes}:{seconds}", (ex. 5:01) [SPACING DOES MATTER]
    <h2>Stopwatch Function: Counts upwards until program is ended</h2>
    <h3>stopwatch()</h3>
      <h4>Function takes no arguments</h4>  
      <h2>World Time Clock: Returns the local time of given city</h2>
      <h3>world_time(input)</h3>
      <h4>The 'input' parameter should be a single string that is structured: "{region}/{city}" or "{timezone}", (ex. America/Chicago or ROC) [SPACING DOES MATTER]</h4>
      <h4>Pay a vist to <a href="https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568">this page</a> to see what the acceptable timezones are</h4>
