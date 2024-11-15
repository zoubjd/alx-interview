#!/usr/bin/node
const exec = require('child_process').exec;

let child = exec("timeout 60s ./0-starwars_characters.js 3", function(error, stdout, stderr) {
  if (error) console.log(error);
  listCharacters = ["Luke Skywalker", "C-3PO", "R2-D2", "Darth Vader", "Leia Organa", "Obi-Wan Kenobi", "Chewbacca", "Han Solo", "Jabba Desilijic Tiure", "Wedge Antilles", "Yoda", "Palpatine", "Boba Fett", "Lando Calrissian", "Ackbar", "Mon Mothma", "Arvel Crynyd", "Wicket Systri Warrick", "Nien Nunb", "Bib Fortuna"];
  
  stdoutLines = stdout.split("\n");
  for (let index = 0; (index < stdoutLines.length) && (listCharacters.length > 0); index++) {
      let line = stdoutLines[index];
      if (line != listCharacters[0]) {
        console.log(line + " instead of " + listCharacters[index]);
        break;
      }
      listCharacters.splice(0, 1);
  }

  if (listCharacters.length == 0) {
    process.stdout.write("OK");
  }
  else {
    console.log("Characters not found");
    console.log(listCharacters);
  }
});