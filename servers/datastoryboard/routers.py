from fastapi.routing import APIRouter

datastoryboard = APIRouter(
    prefix='/api/v1/dsb/report1401',
    tags=['datastoryboard'],
)


@datastoryboard.get('/{slug}')
async def retrieve(slug: str):
    return {
        "id": 1,
        "title": "عنوان تستی",
        "slug": slug,
        "seo_description": "seoDescription",
        "seo_og_image": "http://127.0.0.1:8000/dsb-media/report1401ogimages/download.jpeg",
        "title_color_code": "12",
        "bg_color_code": "12",
        "bg_image_desktop": "http://127.0.0.1:8000/dsb-media/report1401chapterintrobg/download.jpeg",
        "bg_image_mobile": "http://127.0.0.1:8000/dsb-media/report1401chapterintrobg/download_e8rgZo8.jpeg",
        "bg_image_desktop_blur_base64": "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",
        "bg_image_mobile_blur_base64": "iVBORw0KGgoAAAANSUhEUgAAACIAAAAWCAIAAAAqztkuAAAG40lEQVR4nAXB249dVRkA8G9961trr3055+yZOb1QqLadXhhIQYEEsYVAg4o88GRiwqsSHnzlDyCRaPRZE0yUGEKEiASiMQTkQVE0JApYQNr0yqW0nWmn55x99mXdvuXvJ15//S/THTvisNw6//H7Z66kor7/2L0bh/YzMyICgAAxn3dvXLBxGA4OH9z2tbvVZNf757b/81m/BsODR9dWJibESEQA+PGH/3jx+Z/eed/3Hz7xqO17k48j89bVTfrjn9/ac8tXD1VX94tPbz98/H+X7NmzZzYOH5BSEpGUMoRYlvmtNQdPeyb3RLvw5y9cvph24Y6H7t61Oil8iAoRUYbox6O1jX1H7tg4dP7022UxcmLSLuzf//qK+PVvX0RUu9dKt2wgdtOdu6WpbNsYo4t6ZwK4vHl9cMHbHtlb75UpSRIH770DMlLK1XGxtlKiCM1sKyXWhNH52aJFJKXUMz97emVk6dsnjofgL5w5bQoCzvPRhEwVvQNIMUZSRJiqXHkSKVgUCZEFBEhOE1AmtVKaRHALFFZRFBxk8kKqLC9DiCnx/gM3Hz/+XRIgrly+OmjMQWQRiAfpWQuvdI4SiWRZGCFEcCJ5pjAE1wqBClFqkxWZKSutCeKMWZJelexhuEYgrCDvnXX2h08+PV3bRZG5KPLT2+dztmtCZMtNxhRdSmmSkvA+7/ue+yH1Azvfzub9jVlKAJku60ks+zixtsgQW1LGFJOMRNtcZ479gLP50DaL9TvXmAM9/uovd+7afbwPmZFYT0dKKwQlUeaVoCwCBGubK5u+WUbn/LJNi6UAkfKs9b6bzU3b5tO6moisFCZLyD6E4IRhXVIlhScGUWRE/33zreGbR++qDwgzDpM1OZkWEEPgRKVAmYQs80KPJ0llwdrGRoZeIILKsrJSeS7zHEmRVplWyG0YWk4RtRmbUV4UEvCJn7/8+Inbafre1aXDyw+Mdkiv5pMKIkqVqVwqUEoh6TzPsyKXkpzAgTkNHoXwUhqkPM9lWSaTIxkflXPBD9B5wyykX4YQ265TSvzkpXcoYHbzrP9iMUsqDgqHzS+XaEpd6WptuuOmvBo755IPMsTUdmnWhBszFAJShK73mY6KWEthlQuQgucAXaBhGPwwbM9mn1+9/uMfPPrUs29QAN5bFoiy0KYkVRXVpJxWptb5qF6dSlK+s04pwYCkinpiIwOAHlVFVUFuVFVRPaFRCYgieo7RmLK3wbZNZLvZaOGbtXSZSiPP7auPliu63mtG9XhcV6NpqYoY2Xlm13fOzbsOl72bz1kiTlcIpUfRMvthyJwrE0OM7AOmCBxRJEWsS6VkDcK//dKv1ttTdO34evvA0ROLGlTVB+r71OqAKcbgfZyjJA8IZTnYMJBiiomZJKks47yMhcG8sCBd28fgJSQECMxdP3jnUoo2iq8cXG9tR/ldRw6WO/UgA4Nr+mEIi4icBwDQikyea63l6tqMAQGht8wslJJZjlWBuS7rsQDwtvchAgpUSgj2kZu2JZG04D0r0K404t1PPtq+5k5fOzXOq4pxgrIcr0wmEwBkjiBE5ORDnM0Xi0XrOsuJEWVmjCkLyqiejDmyd97bQUskIRAheN8s5hIiJ/fMC//aUwWxdXnzT/88o6rFWOeV0lqIYjSqR6OYYOg663w32LbtbswbnyByUjqTUkoUwGzdUI9HBCmBiN5WlFJgIC1EWjZNSkkI3ubR1ryjdugO7V11XgmUEiHG4GNiSEIAkQwxSiml0qbIdYLBuqFtfAiktdGZ95GHRqWOE7IdUKWusy6rSUkJfQLwiR6+9whHJm2yrv+iJB2CJxJCAAFD8CCSkgCKQgisKThpndMCIiSGlFJCFLFfeNsOEiCftg4VhBCj8zYy1PmQZ4lM7h0IRAyB/332tFGiIK40TEdZnYFkh8wkpcmUSpxsJ7wF7zCFFCx4SxDHRZbLFPpuGWgpRk1Qy+XQ9320LjkPPlKKBn1w54QUZPvhvkNHlsvO+iFTypUi16iIKTOSlO071y9918iEpdEqM4Zk33cRIJdgpfAxxuDqXFaqqEMfWHoqOEZByYUWhnDr6h8WQ4khho1D6yRCP/MbYn7TjZMraHfdcjAmuPLZxWtfXjp8x917961vn/3wb7/7zRsvvjDbunLs/mP79+198/fPv/P6q4eOfeehbz2ybhafXKOXPxIX3M4DB48U8NluavqrV85dmp366PORek98cursuChOnjz57GsfP7ZRNMutw0cO3PaNE8F3RVmozLTXt1977hfnzlx47IkfHf36XUQUnBUoL168+NzTTx373pMPPPIgERHHBAkYAiA1l+afvvtlo+Zyr5+98uA9l/4PJV4WDiQCluQAAAAASUVORK5CYII=",
        "overriding_component_code": "124",
        "datetime_added": "2023-05-06T18:54:32.286793+03:30",
        "datetime_last_edit": "2023-05-06T19:19:17.184098+03:30",
        "order": 1,
        "is_published": True,
        "last_author": None,
        "sections": [
            {
                "id": 1,
                "chapter": 1,
                "title": "test",
                "bg_color_code": "564564",
                "bg_image_desktop": None,
                "bg_image_mobile": None,
                "bg_image_desktop_blur_base64": "",
                "bg_image_mobile_blur_base64": "",
                "order_for_chapter": 2,
                "datetime_added": "2023-05-06T19:19:17.186008+03:30",
                "datetime_last_edit": "2023-05-07T22:30:37.166757+03:30",
                "is_published": True,
                "last_author": 1,
                "section_added_components": [],
                "section_image_widgets": [],
                "section_paragraph_widgets": [
                    {
                        "id": 1,
                        "content": "لورم ایپسوم یا طرح‌نما (به انگلیسی: Lorem ipsum) به متنی آزمایشی و بی‌معنی در صنعت چاپ، صفحه‌آرایی و طراحی گرافیک گفته می‌شود. طراح گرافیک از این متن به عنوان عنصری از ترکیب بندی برای پر کردن صفحه و ارایه اولیه شکل ظاهری و کلی طرح سفارش گرفته شده استفاده می نماید، تا از نظر گرافیکی نشانگر چگونگی نوع و اندازه فونت و ظاهر متن باشد. معمولا طراحان گرافیک برای صفحه‌آرایی، نخست از متن‌های آزمایشی و بی‌معنی استفاده می‌کنند تا صرفا به مشتری یا صاحب کار خود نشان دهند که صفحه طراحی یا صفحه بندی شده بعد از اینکه متن در آن قرار گیرد چگونه به نظر می‌رسد و قلم‌ها و اندازه‌بندی‌ها چگونه در نظر گرفته شده‌است. از آنجایی که طراحان عموما نویسنده متن نیستند و وظیفه رعایت حق تکثیر متون را ندارند و در همان حال کار آنها به نوعی وابسته به متن می‌باشد آنها با استفاده از محتویات ساختگی، صفحه گرافیکی خود را صفحه‌آرایی می‌کنند تا مرحله طراحی و صفحه‌بندی را به پایان برند.",
                        "section": 1
                    }
                ],
                "section_video_widgets": []
            }
        ],
        "intro_added_components": [],
        "intro_image_widgets": [],
        "intro_paragraph_widgets": [],
        "intro_video_widgets": []
    }
