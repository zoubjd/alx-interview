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
    for (let i = 0; i < data.characters.length; i++) {
      request(data.characters[i], (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
