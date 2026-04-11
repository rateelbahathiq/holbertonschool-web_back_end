const express = require('express');
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);

      let output = `Number of students: ${students.length}`;
      const fields = {};

      students.forEach((student) => {
        const [firstName, , , field] = student.split(',');

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstName);
      });

      Object.keys(fields).forEach((field) => {
        output += `\nNumber of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
      });

      resolve(output);
    });
  });
}

const app = express();

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.type('text/plain');

  countStudents(process.argv[2])
    .then((data) => {
      res.send(`This is the list of our students\n${data}`);
    })
    .catch(() => {
      res.send('This is the list of our students\nCannot load the database');
    });
});

app.listen(1245);

module.exports = app;
