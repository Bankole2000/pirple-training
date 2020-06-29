const mainArea = document.querySelector('main');
const header = document.querySelector('header');
const messageArea = document.querySelector('.message-box');
const messageSpan = document.querySelector('.message');
const pageList = ['index', 'signup', 'login', 'addTodo'];
const actionList = [
  'addTodo',
  'addTodoItem',
  'login',
  'logout',
  'signup',
  'cancel',
];
const emailRegex = /^[a-z]+(_|\.)?[a-z0-9]*@[a-z]+\.[a-z]{2,}$/i;
const passwordRegex = /^[0-9a-zA-Z$&!@#%^*(){}"'\[\];:<>/\\?+=_.-\|]{6,}$/;
const nameRegex = /^[a-z]{2,}$/i;
let loggedInUser = {};

// Event Listeners
document.addEventListener('click', (e) => {
  if (pageList.indexOf(e.target.classList[0]) > -1) {
    e.preventDefault();
    mainArea.innerHTML = pages[e.target.classList[0]];
    return;
  }

  if (actionList.indexOf(e.target.id) > -1) {
    actions[e.target.id](e);
    return;
  }
});

// functions
const showMessage = (message, success, time) => {
  let bgStyle = success ? 'forestgreen' : 'tomato';
  messageArea.style.background = bgStyle;
  messageArea.style.height = '40px';
  messageArea.style.padding = '5px';
  messageSpan.textContent = message;
  setTimeout(() => {
    hideMessage();
  }, time * 1000);
};
const hideMessage = () => {
  messageArea.style.height = '0px';
  messageArea.style.padding = '0px';
  messageArea.style.background = 'grey';
  messageSpan.textContent = '';
};
const loginUser = (email, password, callback) => {
  store.getAll('users', (err, data) => {
    if (!err) {
      console.log(err, data);
      for (user in data.SuccessData['users']) {
        if (
          data.SuccessData['users'][user]['email'] == email &&
          data.SuccessData['users'][user]['password'] == password
        ) {
          loggedInUser = data.SuccessData['users'][user];
          callback(false, { Error: false, Message: 'Login Successful' });
          prepareDashboard(loggedInUser);
          return;
        }
      }
      callback(true, { Error: true, Message: 'Incorrect Login Details' });
    } else {
      callback(true, data);
    }
  });
};
const createUUID = () => {
  strLength = 20;
  strLength = typeof strLength == 'number' && strLength > 0 ? strLength : false;
  if (strLength) {
    // define all possible characters that could go into a string
    const possibleCharacters = 'abcdefghijklmnopqrstuvwxyz0123456789';

    // Start the final string
    let str = '';
    for (i = 1; i <= strLength - 13; i++) {
      // Get a random character and append to final string
      const randomCharacter = possibleCharacters.charAt(
        Math.floor(Math.random() * possibleCharacters.length)
      );
      str += randomCharacter;
    }
    return (str += `-${Date.now().toString()}`);
  } else {
    return false;
  }
};

const prepareAccount = (user) => {
  html = `<section class="content" id="app">
  <input type="hidden" name="user-id" />
  <h1>Account Settings</h1>
  <ul class="account-list">
    <li>
      <h4>First Name: </h4>
      <input
        type="text"
        class="todo-item"
        placeholder="${user.firstName}"
      />
    </li>
    <li>
      <h4>Last Name: </h4>
      <input
        type="text"
        class="todo-item"
        placeholder="${user.lastName}"
      />
    </li>
    <li>
      <h4>Email: </h4>
      <input
        type="text"
        class="todo-item"
        placeholder="${user.email}"
      />
    </li>
    <li>
      <h4>Password: </h4>
      <input
        type="text"
        class="todo-item"
        placeholder="Password"
      />
    </li>
    <li>
      <h4>Confirm Password: </h4>
      <input
        type="text"
        class="todo-item"
        placeholder="Confirm Password"
      />
    </li>
  </ul>
  <button>Update ⚙️</button>
  <button onclick='return prepareDashboard(loggedInUser)'>Back ❌</button>
</section>`;
  mainArea.innerHTML = html;
  return false;
};

const prepareEditTodo = (id) => {
  store.get('todos', id, (err, data) => {
    if (!err) {
      showMessage('Fetched Todo', true, 2);
      console.log(data);
      let html = `<section class="content">
      <input type="hidden" name="user-id" value="${user.id}"/>
      <h1>${data.SuccessData.name}</h1>
      <ul class="todo-list">`;
      let todos = data.SuccessData.items;
      for (todo in data.SuccessData.items) {
        console.log(todo);
        html += `<li>
        <input
      type="checkbox"
      class="todo-checkbox"
      for="${todos[todo].id}"
      
    />
        <input
      type="text"
      class="todo-item"
      placeholder="${todos[todo].item}"
      id="${todos[todo].id}"
      value="${todos[todo].item}"
      
    />
        <div>
        <button class="item-action" onclick='actions.addNewTodoItem(event, this)'><span class="addTodoItem "
        >➕ <span class="item-action-text">Add</span></span
      ></button>
          
  <button class="item-action" onclick='actions.deleteTodoItem(event, this)'><span class="deleteTodoItem item-action" 
    >❌ <span class="item-action-text">Delete</span></span
  ></button>
        </div>
      </li>`;
      }
      html += `</ul>
        <button onclick='actions.saveTodoList(event, loggedInUser)'>Update 💾</button>  
        <button onclick='return prepareDashboard(loggedInUser)'>Cancel ❌</button>
        </form>
        </section>`;
      mainArea.innerHTML = html;
    } else {
      showMessage('Failed to get todo data', false, 2);
      console.log(data);
    }
  });
};

const prepareDashboard = (user) => {
  const gravatar = MD5(user.email.trim().toLowerCase());
  user.image = `https://www.gravatar.com/avatar/${gravatar}`;
  let headerhtml = `<div class="user-profile">
  <img src="${user.image}" alt="Profile Image" />
  <a onclick='return prepareAccount(loggedInUser)' >
    Account Settings
  </a>
</div>
<nav>
  <a id="logout">Log out</a>
</nav>`;
  let html = `<section class="content">
  <input type="hidden" name="user-id" value="${user.id}"/>
  <h1>${user.firstName}'s Todo List</h1>
  <ul class="todo-list">`;
  if (user.todos.length > 0) {
    user.todos.forEach((todo) => {
      store.get('todos', todo, (err, data) => {
        if (!err) {
          console.log(data);
          html += `<li onclick="prepareEditTodo('${todo}')" style="cursor: pointer;">
      <span class="text">${data.SuccessData.name}</span>
      <div>
        <span class="votes">${moment(data.SuccessData.created).fromNow()}</span>
        
<button class="item-action" onclick='actions.deleteTodoItem(event, this)'><span class="deleteTodoItem item-action" 
  >❌ <span class="item-action-text">Delete</span></span
></button>
      </div>
    </li>`;
        } else {
          console.log(data);
        }
      });
    });
  } else {
    html += `<li>
    <span class="text">Sorry ${user.firstName}. It seems you don't have any todo's right now</span>
    <div>
      
    </div>
  </li>`;
  }
  html += `</ul>
  <a class="addTodo">
    <button class="addTodo">Add A todo ✏️</button>
  </a>
</section>`;

  mainArea.innerHTML = html;
  header.innerHTML = headerhtml;
  return false;
};

// Actions Object for actions
const actions = {};

actions.checkInputs = (inputArray) => {
  let result;
  inputArray.forEach((input) => {
    if (input.value.trim() === '') {
      result = false;
    } else {
      result = true;
    }
  });
  return result;
};
actions.logout = () => {
  mainArea.innerHTML = pages['index'];
  headerHTML = `<a class="index">
  Todo Mngr
</a>

<nav>
  <a class="signup">Sign up</a>
  <a class="login">Login</a>`;
  header.innerHTML = headerHTML;
  showMessage('You Logged out', false, 2);
};
actions.login = (e) => {
  e.preventDefault();
  let form = mainArea.querySelector('form');
  let email = form.email.value;
  let password = form.password.value;
  email =
    typeof email == 'string' &&
    email.trim().length > 0 &&
    emailRegex.test(email.trim())
      ? email.trim()
      : false;
  password =
    typeof password == 'string' &&
    password.trim().length > 0 &&
    passwordRegex.test(password.trim())
      ? MD5(password.trim())
      : false;
  if (email && password) {
    loginUser(email, password, (err, data) => {
      if (!err) {
        showMessage(data.Message, !err, 1);
        console.log(data.Message);
      } else {
        showMessage(data.Message, !err, 2);
        console.log(err, data);
      }
    });
  } else {
    showMessage('Invalid Login Details', false, 2);
  }
  console.log(form, email, password);
};
actions.signup = (e) => {
  e.preventDefault();
  let form = mainArea.querySelector('form');
  let email = form.email.value;
  let firstName = form.firstName.value;
  let lastName = form.lastName.value;
  let password = form.password.value;
  let cpassword = form.cpassword.value;
  let tos = form.tos.checked;
  email =
    typeof email == 'string' &&
    email.trim().length > 0 &&
    emailRegex.test(email.trim())
      ? email.trim()
      : false;
  firstName =
    typeof firstName == 'string' &&
    firstName.trim().length > 1 &&
    nameRegex.test(firstName.trim())
      ? firstName.trim()
      : false;
  lastName =
    typeof lastName == 'string' &&
    lastName.trim().length > 1 &&
    nameRegex.test(lastName.trim())
      ? lastName.trim()
      : false;
  password =
    typeof password == 'string' &&
    password.trim().length > 0 &&
    passwordRegex.test(password.trim())
      ? MD5(password.trim())
      : false;
  if (email && password && firstName && lastName && tos) {
    if (password == MD5(cpassword)) {
      const id = createUUID();
      const newUser = {
        id,
        firstName,
        lastName,
        email,
        password,
        tos,
        todos: [],
      };

      store.getAll('users', (err, data) => {
        if (!err) {
          for (user in data.SuccessData['users']) {
            console.log(data.SuccessData['users']);
            console.log(data.SuccessData['users'][user]['email']);
            if (data.SuccessData['users'][user]['email'] == email) {
              showMessage('This Email is already Registered', false, 2);
              return;
            }
          }
          store.add('users', newUser, (err, data) => {
            if (!err) {
              showMessage('Registration Successful', !err, 2);
              console.log(err, data);
              loggedInUser = newUser;
              prepareDashboard(loggedInUser);
            } else {
              showMessage(data.Message, err, 2);
              console.log(err, data);
            }
          });
        } else {
          store.add('users', newUser, (err, data) => {
            if (!err) {
              showMessage('Registration Successful', !err, 2);
              console.log(err, data);
              loggedInUser = newUser;
              prepareDashboard(loggedInUser);
            } else {
              showMessage(data.Message, err, 2);
              console.log(err, data);
            }
          });
        }
      });
    } else {
      showMessage('Passwords do not match', false, 2);
    }
  } else {
    showMessage('Incomplete Registration Details', false, 2);
  }
};
actions.addNewTodoItem = function (e, element) {
  e.preventDefault();
  let what = element;
  console.log(what, e.target);
  let newInput = document.createElement('input');
  newInput.type = 'text';
  newInput.className = 'todo-item';
  newInput.placeholder = 'New Todo List Item';
  let newDiv = document.createElement('div');
  newDiv.innerHTML = `<button class="item-action" onclick='actions.addNewTodoItem(event, this)'><span class="addTodoItem item-action" 
  >➕ <span class="item-action-text">Add</span></span
></button>
<button class="item-action" onclick='actions.deleteTodoItem(event, this)'><span class="deleteTodoItem item-action" 
  >❌ <span class="item-action-text">Delete</span></span
></button>`;
  let newLi = document.createElement('li');
  newLi.appendChild(newInput);
  newLi.appendChild(newDiv);
  document.querySelector('.todo-list').appendChild(newLi);
};

actions.deleteTodoItem = function (e, element) {
  e.preventDefault();
  let itemToDelete = element.parentElement.parentElement;
  console.log(itemToDelete, e.target);
  itemToDelete.remove();
};

actions.saveTodoList = function (e, user) {
  let form = document.querySelector('#createNewTodo');
  let userId = user.id;
  let todoItems = form.querySelectorAll('input');
  e.preventDefault();
  console.log(todoItems, e.target, userId);
  let todoListName =
    typeof todoItems[0].value == 'string' &&
    todoItems[0].value.trim().length > 0
      ? todoItems[0].value.trim()
      : false;
  let todoListItems = Array.from(todoItems);
  todoListItems.shift();
  let inputsOkay = actions.checkInputs(todoListItems);
  console.log(inputsOkay, todoListName, todoListItems);
  if (todoListName && inputsOkay) {
    let todoId = createUUID();
    newTodoList = {};
    newTodoList.id = todoId;
    newTodoList['name'] = todoListName;
    newTodoList['items'] = {};
    newTodoList['owner'] = userId;
    newTodoList['created'] = Date.now();
    user.todos.push(todoId);
    todoListItems.forEach((todoItem) => {
      let itemId = createUUID();
      newTodoList['items'][itemId] = {
        id: itemId,
        item: todoItem.value,
        completed: false,
        created: Date.now(),
      };
    });
    console.log(newTodoList, user);
    store.add('todos', newTodoList, (err, data) => {
      if (!err) {
        store.update('users', user.id, user, (userUpdateErr, userdata) => {
          if (!userUpdateErr) {
            showMessage('User Updated in local storage', true, 2);
            prepareDashboard(user);
            console.log(userdata);
          } else {
            showMessage('Failed to update user in local storage', false, 2);
            console.log(userdata);
          }
        });
        showMessage('Todo Added to local storage', true, 2);
        console.log(data);
      } else {
        showMessage('Failed to add todos', false, 2);
        console.log(data);
      }
    });
  } else {
    showMessage('Missing Required Fields', false, 2);
  }
};

// Pages object for pages
const pages = {};

pages.signup = `<div class="center-block">
<h2>Register</h2>
<form action="" class="register">
<input type="firstName" name="firstName" placeholder="First Name" />
<input type="lastName" name="lastName" placeholder="Last Name" />
  <input type="text" name="email" placeholder="Email" />
  <input type="password" name="password" placeholder="Password" />
  <input type="password" name="cpassword" placeholder="Confirm Password" />
  <input type="checkbox" id="tos" name="tos" value="tos">
  <label for="tos"> I Agree to terms of use</label><br>

  <button id="signup">Register</button>
  
</form>
<div>
  Got an Account?
  <a class="login">Login Instead</a>
</div>
</div>`;
pages.login = `<div class="center-block">
<h2>Login</h2>
<form action="" class="login">
  <input type="text" name="email" placeholder="Email" />
  <input type="password" name="password" placeholder="Password" />
  <button id="login">login</button>
  
</form>
<div>No Account? <a class="signup">Register Instead</a></div>
</div>`;
pages.dashboard = ``;
pages.account = ``;
pages.addTodo = `<section class="content" id="app">
<form id="createNewTodo">
<h1 id="todoTitle">New Todo List</h1>

<input type="text" placeholder="New Todo List Name" required/>
<ul class="todo-list">
  <li>
    <input
      type="text"
      class="todo-item"
      placeholder="New Todo List Item"
      
    />

    <div>
      <button class="item-action" onclick='actions.addNewTodoItem(event, this)'><span class="addTodoItem "
        >➕ Add</span
      ></button>
     
    </div>
  </li>
</ul>
<button onclick='actions.saveTodoList(event, loggedInUser)'>Save 💾</button>  
<button onclick='return prepareDashboard(loggedInUser)'>Cancel ❌</button>
</form>
</section>`;
pages.index = `<section id="content">
<h1>Welcome to the Todo List Manager</h1>
<div class="main-area">
  <button class="signup">signup</button>
  <button class="login">login</button>
</div>
</section>`;

// Storage Object for functions
const store = {};

// Storage Methods
store.add = (type, data = {}, callback) => {
  if (localStorage.getItem(type)) {
    let prevData = JSON.parse(localStorage.getItem(type));
    prevData[type][data.id] = data;
    localStorage.setItem(type, JSON.stringify(prevData));
    callback(false, {
      Error: false,
      Message: `New ${type} Saved to Local Storage`,
    });
  } else {
    newData = {};
    newData[type] = {};
    newData[type][data.id] = data;
    newData = JSON.stringify(newData);
    localStorage.setItem(type, newData);

    callback(false, {
      Error: false,
      Message: `New ${type} Saved to Local Storage`,
    });
  }
};

store.getAll = (type, callback) => {
  if (localStorage.getItem(type)) {
    let data = JSON.parse(localStorage.getItem(type));
    if (data) {
      callback(false, {
        Error: false,
        Message: `Retrieved all ${type} data`,
        SuccessData: data,
      });
    } else {
      callback(true, {
        Error: true,
        Message: `Couldn't find any ${type} with the id - ${id}`,
      });
    }
  } else {
    callback(true, {
      Error: true,
      Message: `Couldn't find any ${type} in Local Storage`,
    });
  }
};

store.get = (type, id, callback) => {
  if (localStorage.getItem(type)) {
    let data = JSON.parse(localStorage.getItem(type));
    if (data[type][id]) {
      callback(false, {
        Error: false,
        Message: `Retrieved data from ${type} with id - ${id}`,
        SuccessData: data[type][id],
      });
    } else {
      callback(true, {
        Error: true,
        Message: `Couldn't find any ${type} with the id - ${id}`,
      });
    }
  } else {
    callback(true, {
      Error: true,
      Message: `Couldn't find any ${type} in Local Storage`,
    });
  }
};

store.update = (type, id, data, callback) => {
  if (localStorage.getItem(type)) {
    prevData = JSON.parse(localStorage.getItem(type));
    if (prevData[type][id]) {
      prevData[type][id] = data;
      localStorage.setItem(type, JSON.stringify(prevData));
      callback(false, {
        Error: false,
        Message: `${type} with Id - ${id} Updated`,
      });
    } else {
      callback(true, {
        Error: true,
        Message: `Couldn't find ${type} with that Id - ${id}`,
      });
    }
  } else {
    callback(true, {
      Error: true,
      Message: `Couldn't find any ${type} in Local Storage`,
    });
  }
};

store.delete = (type, id, callback) => {
  if (localStorage.getItem(type)) {
    let data = JSON.parse(localStorage.getItem(type));
    if (data[id]) {
      delete data[id];
      if (localStorage.setItem(type, JSON.stringify(data))) {
        callback(false, {
          Error: false,
          Message: `${type} with Id - ${id} Updated`,
        });
      } else {
        callback(true, {
          Error: true,
          Message: `Couldn't delete ${type} with that Id - ${id} in local Storage`,
        });
      }
    } else {
      callback(true, {
        Error: true,
        Message: `Couldn't find ${type} with that Id - ${id} in Local Storage`,
      });
    }
  } else {
    callback(true, {
      Error: true,
      Message: `Couldn't find any ${type} in Local Storage`,
    });
  }
};
