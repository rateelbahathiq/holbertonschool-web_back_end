# ES6 Data Manipulation

## 📚 Description
This project introduces **ES6 data manipulation techniques** using arrays, typed arrays, sets, and maps in modern JavaScript.

---

## 📖 Concepts Covered
- Using `map()` to transform arrays
- Using `filter()` to select specific data
- Using `reduce()` to combine values
- Working with `ArrayBuffer` and `DataView`
- Creating and using typed arrays
- Using `Set` for unique values
- Checking values in a `Set`
- Cleaning and formatting `Set` data
- Creating and updating `Map`
- Iterating through `Map` entries
- Updating `Map` values dynamically

---

## 📂 Files

| File | Description |
|---|---|
| `0-get_list_students.js` | Returns an array of student objects |
| `1-get_list_student_ids.js` | Returns an array of student IDs using `map()` |
| `2-get_students_by_loc.js` | Filters students by city using `filter()` |
| `3-get_ids_sum.js` | Returns the sum of student IDs using `reduce()` |
| `4-update_grade_by_city.js` | Updates student grades by city using `filter()` + `map()` |
| `5-typed_arrays.js` | Creates an `ArrayBuffer` with an `Int8` value |
| `6-set.js` | Creates a `Set` from an array |
| `7-has_array_values.js` | Checks if all array values exist in a `Set` |
| `8-clean_set.js` | Cleans set values based on a prefix string |
| `9-groceries_list.js` | Creates a grocery `Map` |
| `10-update_uniq_items.js` | Updates unique grocery items in a `Map` |

---

## 💻 Example Usage

### getListStudentIds
```javascript
import getListStudents from './0-get_list_students.js';
import getListStudentIds from './1-get_list_student_ids.js';

console.log(getListStudentIds(getListStudents()));
```

### Output
```javascript
[1, 2, 5]
```

---

## 👩‍💻 Author
**Rateel Bahathek**
