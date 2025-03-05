# Personal Tasks Repository

This repository is designed for submitting individual programming tasks for the Advanced Python course. Please follow these instructions carefully to submit your work.

## Repository Structure

Each student has their own designated folder within this repository. You only have write access to your personal folder as specified in the CODEOWNERS file.

## How to Submit Your Tasks

### 1. Initial Setup
```bash
# Clone the repository
git clone <repository-url>
cd Personal-Tasks

# Create and switch to a new branch for your task
git checkout -b task/your-name/task-name
```

### 2. Adding Your Work
- Place your files ONLY in your designated folder
- Make sure to include:
  - Source code files (.py)
  - Requirements.txt (if needed)
  - Brief documentation explaining your solution

### 3. Committing and Pushing
```bash
# Add your changes
git add your-folder/*

# Commit with a descriptive message
git commit -m "Add solution for Task X"

# Push to your branch
git push origin task/your-name/task-name
```

### 4. Creating a Pull Request
1. Go to the repository on GitHub
2. Click on "Pull Requests" and then "New Pull Request"
3. Select your branch as the source
4. Write a clear description of your changes
5. Submit the pull request

## Important Notes

- ⚠️ Never commit directly to the main branch
- ⚠️ Only modify files within your designated folder
- ✅ Each task should be submitted in a separate branch
- ✅ Wait for the instructor's review before merging
- ❌ Pull requests modifying other students' folders will be rejected

## Best Practices

1. Keep your commits atomic and well-described
2. Test your code thoroughly before submitting
3. Follow the Python style guide (PEP 8)
4. Include proper documentation
5. Respond to review comments promptly

## Student Folder Structure

### Setting Up Your Personal Folder
1. Copy the `student-readme-template.md` to your folder
2. Rename it to `README.md`
3. Fill in your information
4. Update it after completing each task

### Folder Organization
```
your-name/
├── README.md           # Your progress tracking document
├── Session-1/             # Each task in its own folder
│   ├── file1
│   ├── file2
│   └── README.md
├── Session-2/
│   ├── file1
│   ├── file2
│   └── README.md
...
```

## Need Help?

If you encounter any issues with the submission process, please contact the course instructor or teaching assistants.

---

<div dir="rtl">

# مخزن تکالیف فردی

این مخزن برای ارسال تکالیف برنامه‌نویسی فردی دوره پایتون پیشرفته طراحی شده است. لطفاً این دستورالعمل‌ها را برای ارسال کار خود با دقت دنبال کنید.

## ساختار مخزن

هر دانشجو در این مخزن یک پوشه اختصاصی دارد. شما فقط به پوشه شخصی خود دسترسی نوشتن دارید که در فایل CODEOWNERS مشخص شده است.

## نحوه ارسال تکالیف

### ۱. راه‌اندازی اولیه
```bash
# Clone کردن مخزن
git clone <repository-url>
cd Personal-Tasks

# ایجاد و تغییر به شاخه جدید برای تکلیف
git checkout -b task/your-name/task-name
```

### ۲. اضافه کردن کار
- فایل‌ها را فقط در پوشه تعیین شده خود قرار دهید
- حتماً موارد زیر را شامل شود:
  - فایل‌های کد منبع (.py)
  - Requirements.txt (در صورت نیاز)
  - مستندات مختصر توضیح راه‌حل

### ۳. Commit و Push
```bash
# اضافه کردن تغییرات
git add your-folder/*

# Commit با پیام توصیفی
git commit -m "Add solution for Task X"

# Push به شاخه
git push origin task/your-name/task-name
```

### ۴. ایجاد Pull Request
۱. به مخزن در GitHub بروید
۲. روی "Pull Requests" و سپس "New Pull Request" کلیک کنید
۳. شاخه خود را به عنوان منبع انتخاب کنید
۴. توضیح واضحی از تغییرات بنویسید
۵. درخواست را ثبت کنید

## نکات مهم

- ⚠️ هرگز مستقیماً به شاخه main کامیت نکنید
- ⚠️ فقط فایل‌های داخل پوشه خود را تغییر دهید
- ✅ هر تکلیف باید در یک شاخه جداگانه ارسال شود
- ✅ منتظر بررسی استاد قبل از merge باشید
- ❌ درخواست‌های تغییر پوشه‌های دیگر دانشجویان رد خواهد شد

## بهترین رویکرد ها

۱. کامیت‌های خود را خوب توصیف کنید
۲. کد خود را قبل از ارسال به دقت تست کنید
۳. راهنمای سبک پایتون (PEP 8) را دنبال کنید
۴. مستندات مناسب را شامل کنید
۵. به نظرات بررسی به موقع پاسخ دهید

## ساختار پوشه دانشجو

### راه‌اندازی پوشه شخصی شما
۱. `student-readme-template.md` را به پوشه خود کپی کنید
۲. آن را به `README.md` تغییر نام دهید
۳. اطلاعات خود را پر کنید
۴. پس از تکمیل هر تکلیف آن را به‌روزرسانی کنید

### سازماندهی پوشه
```
your-name/
├── README.md           # سند پیگیری پیشرفت شما
├── Session-1/             # هر تکلیف در پوشه خود
│   ├── file1
│   ├── file2
│   └── README.md
├── Session-2/
│   ├── file1
│   ├── file2
│   └── README.md
...
```

## نیاز به کمک دارید؟

اگر با مشکلاتی در فرآیند ارسال مواجه شدید، لطفاً با استاد دوره یا دستیاران آموزشی تماس بگیرید.

</div>