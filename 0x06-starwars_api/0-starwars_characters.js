#!/usr/bin/node

if (process.argv.length < 3 || isNaN(process.argv[2])) {
  console.log('Usage: ./0-starwars_characters movie_id');
  process.exit(1);
}

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;
    // console.log(characters);
    const fetchcharacters = async (characters) => {
      try {
        const charpromises = characters.map(character => fetch(character).then(response => response.json()));
        const charadata = await Promise.all(charpromises);
        charadata.forEach(character => console.log(character.name));
      } catch (error) {
        console.log(error);
      }
    };
    fetchcharacters(characters);
  }
});
