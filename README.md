## Random Password Generator
This program allows you to create multiple random passwords of varying lengths that include lowercase letters, uppercase letters, and numbers.
### How to Use
After running the program, you need to enter the number of passwords you want to generate and the desired length of each password. The program will then generate and display the random passwords.

### How it Works
The `generate_password` function takes a list of password lengths and for each length, generates a random password using lowercase letters from the alphabet. It then replaces some of the characters with numbers and uppercase letters.

`main` gets the number of passwords and their lengths from the user, generates the passwords using `generate_password`, and displays them.

### Sample Output
```
How many passwords do you want to generate? 3
Enter length of password #1: 8
Enter length of password #2: 10
Enter length of password #3: 6
Generated passwords: ['fzjg8J5e', 'sznuD7bNwG', 'yjvQ5h']
```

## تولید کننده رمز عبور تصادفی

این برنامه به شما اجازه می‌دهد تا چند رمز عبور تصادفی با طول دلخواه بسازید که شامل حروف کوچک، اعداد و حروف بزرگ هستند.

### نحوه استفاده
پس از اجرای برنامه، شما باید تعداد رمزهای مورد نظر خود و طول هر یک را وارد نمایید. سپس برنامه رمزهای تصادفی را تولید و نمایش خواهد داد.

### نحوه عملکرد
ابتدا `generate_password` یک لیست از طول هر رمز عبور دریافت و برای هر طول، یک رمز عبور تصادفی با استفاده از حروف کوچک الفبا تولید می‌کند. سپس، برای هر رمز عبور، تعدادی از ارقام و حروف بزرگ را درون رمز جایگزین می‌کند.

### نمونه خروجی
```
How many passwords do you want to generate? 3
Enter length of password #1: 8
Enter length of password #2: 10
Enter length of password #3: 6
Generated passwords: ['fzjg8J5e', 'sznuD7bNwG', 'yjvQ5h']
```
