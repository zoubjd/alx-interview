#!/usr/bin/node
const exec = require('child_process').exec;

let child = exec("timeout 60s ./0-starwars_characters.js 5", function(error, stdout, stderr) {
  if (error) console.log(error);
  listCharacters = ["C-3PO", "R2-D2", "Owen Lars", "Beru Whitesun lars", "Obi-Wan Kenobi", "Anakin Skywalker", "Yoda", "Palpatine", "Boba Fett", "Nute Gunray", "PadmÃ© Amidala", "Jar Jar Binks", "Watto", "Shmi Skywalker", "Ayla Secura", "Mace Windu", "Ki-Adi-Mundi", "Kit Fisto", "Plo Koon", "Mas Amedda", "Gregar Typho", "CordÃ©", "Cliegg Lars", "Poggle the Lesser", "Luminara Unduli", "Barriss Offee", "DormÃ©", "Dooku", "Bail Prestor Organa", "Jango Fett", "Zam Wesell", "Dexter Jettster", "Lama Su", "Taun We", "Jocasta Nu", "R4-P17", "Wat Tambor", "San Hill", "Shaak Ti", "Sly Moore"];
  
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