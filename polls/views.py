from django.http import HttpResponse

import pypdfium2 as pdfium


def index(request,file_name,thumbnail):
    a = "files/"
    c = a + file_name
    pdf = pdfium.PdfDocument(c)
    n_pages = len(pdf)
    page = pdf.get_page(0)
    pil_image = page.render_topil(
            scale=1,
            rotation=0,
            crop=(0, 0, 0, 0),
            greyscale=False,
            optimise_mode=pdfium.OptimiseMode.NONE,
    )
    pil_image.save(f"client/10.png")
    return HttpResponse("Hello, world. You're at the polls indexsss.")
