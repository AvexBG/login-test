const db = require("../routes/db-config");
const bcrypt = require("bcryptjs");

const register = async (req, res) => {
    const { email, username, firstName, lastName, password:Npassword } = req.body
    if (!email || !username || !firstName || !lastName || !Npassword) {
        return res.json({ status: "error", error: "Please enter your email, name, and password" })
    } 
    else {
        db.query('SELECT email, username FROM users WHERE email = ? OR username = ?', [email, username], async (err, result) => {
            if (err) throw err;
            if (result[0]) return res.json({ status: "error", error: "Email or username has already been registered" })
            else {
                const password = await bcrypt.hash(Npassword, 8);
                db.query('INSERT INTO users SET ?', {email: email, username:username, first_name:firstName, last_name:lastName, password: password}, (error, results) => {
                    if (error) throw error;
                    return res.json({ status: "success", success: "User has been registered" })
                })
            }
        })
    }
}
module.exports = register;