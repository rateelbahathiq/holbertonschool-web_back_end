# ES6 Classes

## 📚 Description
This project explores **Object-Oriented Programming (OOP) in ES6** using JavaScript classes.  
It focuses on building classes, using getters and setters, implementing inheritance, static methods, and advanced ES6 features like **Symbols and metaprogramming**.

---

## 📖 Concepts Covered

- Creating classes in ES6
- Writing constructors
- Using getters and setters
- Validating attributes inside classes
- Creating class methods
- Implementing static methods
- Using inheritance with `extends`
- Calling parent constructors with `super`
- Implementing abstract classes
- Overriding methods in subclasses


---

## 📂 Files

| File | Description |
|-----|-------------|
| 0-classroom.js | Creates a basic class with a constructor |
| 1-make_classrooms.js | Creates multiple class instances and returns them in an array |
| 2-hbtn_course.js | Implements getters, setters, and attribute validation |
| 3-currency.js | Creates a class with methods and formatted output |
| 4-pricing.js | Uses another class as an attribute and implements a static method |
| 5-building.js | Implements an abstract class requiring subclasses to override a method |
| 6-sky_high.js | Uses inheritance and method overriding |
| 7-airport.js | Customizes object string representation using `Symbol.toStringTag` |
| 8-hbtn_class.js | Customizes object type conversion using `Symbol.toPrimitive` |
| 9-hoisting.js | Fixes class hoisting and module export issues |
| 10-car.js | Clones objects using `Symbol.species` |

---

## 💻 Example Usage

### Creating a Class

```javascript
class ClassRoom {
  constructor(maxStudentsSize) {
    this._maxStudentsSize = maxStudentsSize;
  }
}
```

---

### Creating Multiple Class Instances

```javascript
import ClassRoom from './0-classroom.js';

function initializeRooms() {
  return [
    new ClassRoom(19),
    new ClassRoom(20),
    new ClassRoom(34),
  ];
}
```

---

## ✍ Author

**Rateel Bahathek**
