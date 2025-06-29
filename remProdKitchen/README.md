# Inventory Management System

A Django-based inventory management system with mobile-responsive design, image uploads, and data export/import functionality.

## Features

- ✅ **Product Management**: Add, edit, delete products
- 📱 **Mobile Responsive**: Works perfectly on phones and tablets
- 🖼️ **Image Upload**: Upload product images
- 📊 **Quantity Management**: Increase/decrease product quantities
- 📁 **Data Export/Import**: Export to JSON/Text, import from files
- 💾 **Backup System**: Create local backups
- 🌐 **Cloud Ready**: Deployed on Vercel

## Tech Stack

- **Backend**: Django 5.2.3
- **Frontend**: Bootstrap 5 + Crispy Forms
- **Database**: SQLite (local) / PostgreSQL (production)
- **Deployment**: Vercel
- **Image Processing**: Pillow

## Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd remProdKitchen
   ```

2. **Install dependencies**
   ```bash
   pipenv install
   ```

3. **Run migrations**
   ```bash
   pipenv run python manage.py migrate
   ```

4. **Start development server**
   ```bash
   pipenv run python manage.py runserver
   ```

5. **Access the application**
   - Local: http://127.0.0.1:8000
   - Network: http://YOUR_IP:8000

## Vercel Deployment

This project is configured for Vercel deployment with the following files:

- `vercel.json`: Vercel configuration
- `requirements.txt`: Python dependencies
- `runtime.txt`: Python version specification
- `build_files.sh`: Build script

### Deployment Steps:

1. **Connect to Vercel**
   ```bash
   vercel login
   vercel
   ```

2. **Set Environment Variables** (in Vercel dashboard):
   - `SECRET_KEY`: Your Django secret key
   - `DEBUG`: False (for production)

3. **Deploy**
   ```bash
   vercel --prod
   ```

## Mobile Access

The application is fully responsive and works on:
- 📱 **Smartphones** (iOS/Android)
- 📱 **Tablets**
- 💻 **Desktop computers**

### Mobile Features:
- Touch-friendly buttons (44px minimum)
- Responsive design
- No zoom on input focus
- Web app capable (add to home screen)

## Data Management

### Export Options:
- **JSON Export**: Structured data for programmatic use
- **Text Export**: Human-readable format
- **Local Backup**: Timestamped backup files

### Import Options:
- **JSON Import**: Import from exported JSON files
- **Smart Updates**: Updates existing or creates new products

## File Structure

```
remProdKitchen/
├── remProd/                 # Main app
│   ├── models.py           # Product model
│   ├── views.py            # Views and logic
│   ├── forms.py            # Forms
│   ├── urls.py             # URL patterns
│   └── templates/          # HTML templates
├── remProdKitchen/         # Project settings
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URLs
│   └── wsgi.py             # WSGI configuration
├── media/                  # Uploaded images
├── backups/                # Backup files
├── requirements.txt        # Python dependencies
├── vercel.json            # Vercel configuration
└── README.md              # This file
```

## Environment Variables

For production deployment, set these environment variables:

- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to 'False' for production
- `DATABASE_URL`: Database connection string (if using external DB)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License. 