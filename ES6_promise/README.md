# ES6 Promises

## 📚 Description
This project explores asynchronous programming in JavaScript using ES6 Promises.

---

## 📖 Concepts Covered
- Creating promises with `new Promise`
- Using `resolve` and `reject`
- Using `Promise.resolve()` and `Promise.reject()`
- Chaining with `.then()`
- Error handling with `.catch()`
- Cleanup with `.finally()`
- Running multiple promises with `Promise.all()`
- Handling all outcomes with `Promise.allSettled()`
- Returning the fastest promise with `Promise.race()`
- Throwing custom errors
- Using `try`, `catch`, and `finally`
- Guarding function execution with error handling

---

## 📂 Files

| File | Description |
|---|---|
| `0-promise.js` | Returns a basic Promise object |
| `1-promise.js` | Returns a resolved or rejected Promise based on a boolean |
| `2-then.js` | Uses `.then()`, `.catch()`, and `.finally()` handlers |
| `3-all.js` | Resolves multiple promises together using `Promise.all()` |
| `4-user-promise.js` | Returns a resolved promise with user data |
| `5-photo-reject.js` | Returns a rejected promise with an Error |
| `6-final-user.js` | Handles multiple promises using `Promise.allSettled()` |
| `7-load_balancer.js` | Returns the first resolved promise using `Promise.race()` |
| `8-try.js` | Throws an error when dividing by zero |
| `9-try.js` | Uses `try/catch/finally` to build a guardrail queue |

---

## 💻 Example Usage

### Basic Promise
```javascript
import getResponseFromAPI from './0-promise.js';

console.log(getResponseFromAPI());
```

### Promise.all Example
```javascript
import handleProfileSignup from './3-all.js';

handleProfileSignup();
```

### Promise.race Example
```javascript
import loadBalancer from './7-load_balancer.js';

const fast = Promise.resolve('fast');
const slow = new Promise((resolve) => setTimeout(resolve, 1000, 'slow'));

console.log(await loadBalancer(fast, slow));
```

---

## ✍ Author
**Rateel Bahathek**e
