# A1-Codes

## Installation Process
1. Fork and clone Repo
2. Run npm install

# Ball Up - Pickup game finder
This application allows the user to browse through Local (v1- Atlanta Only) Parks and create pickup games. Users can also see games that other users have created.
### Technologies Used
- Javascript
- React.js
- React-map-gl
- HTML
- CSS/Sass
- Django
- PostgreSQL
- Axios
### API Routes
| HTTP Method   | URL Path     | Action           | CRUD     |
|:--------------|:-------------|:-----------------|----------|
| GET           | meetup/        | index pickup games    | `R`ead   |
| GET           | park/       | index parks    | `R`ead   |
| GET           | park/<int:pk>/        | show park  | `R`ead   |
| GET           | meetup/<int:pk>/  | show meetup | `R`ead   |
| POST          | meetup/create/        | create meetup           | `C`reate |
| DELETE         | meetup/<int:pk>/edit/`  | delete meetup          | `D`elete |
| PATCH         | meetup/<int:pk>/edit/  | update          | `U`pdate |

# Deployed API Link
[API REPO](https://github.com/OneWay-Laye/ball-up-api)

[API Link](https://ball-up-api.herokuapp.com/)
# Deployed Client Link
[Client Repo](https://github.com/OneWay-Laye/ball-up-client)
# Planning
### ERD
![ERD](https://i.imgur.com/yq6GZRS.png)
### Process & Problem Solving
My process for crating the back end really came from understanding how I wanted my users to interact with the my webpage. I knew I wanted all users even non signed-in users to view parks and pickup games. User must be authenticated in order to create and update pickup games.
### Unsolved Problems For Future Iterations
- Refactoring project to hooks to allows for dynamic update
- More map intrgrations
