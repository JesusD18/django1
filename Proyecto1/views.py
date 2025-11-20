from django.http import HttpResponse

def home(request):
    html = """
    <html>
    <head>
        <title>Bienvenido</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #6a11cb, #2575fc);
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                color: white;
            }
            .card {
                background: rgba(255, 255, 255, 0.15);
                padding: 40px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 20px rgba(0,0,0,0.2);
                text-align: center;
                max-width: 400px;
                width: 90%;
            }
            h1 {
                font-size: 32px;
                margin-bottom: 15px;
            }
            p {
                font-size: 18px;
                margin-bottom: 20px;
            }
            a {
                color: #fff;
                padding: 10px 20px;
                background: rgba(255,255,255,0.25);
                border-radius: 10px;
                text-decoration: none;
                transition: 0.3s;
            }
            a:hover {
                background: rgba(255,255,255,0.4);
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Bienvenido a mi proyecto Django en Vercel</h1>
            <p>Tu despliegue está funcionando correctamente.</p>
            <a href="/admin/">Ir al panel de administración</a>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)
