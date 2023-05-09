from fastapi.routing import APIRouter

datastoryboard = APIRouter(
    prefix='/api/v1/dsb/report1401',
    tags=['datastoryboard'],
)


@datastoryboard.get('/chapters/')
async def chapter_list():
    """
    This API returns the list of all available chapters.
    <br>
    :return: chapters
    """
    return {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [
            {
                "title": "Page_1",
                "slug": "slug",
                "order": 1
            },
            {
                "title": "Page_2",
                "slug": "slug",
                "order": 2
            },
            {
                "title": "Page_3",
                "slug": "slug",
                "order": 3
            },
            {
                "title": "Page_4",
                "slug": "slug",
                "order": 4
            }
        ]
    }


@datastoryboard.get('/chapters/{slug}')
async def get_chapter(slug: str):
    """
    This API returns the master detail of a chapter based on a specified slug.
    <br>
    :param slug: required, string, unique
    <br>
    :return: chapter, json
    """
    return {
        "title": "گزارش اول",
        "slug": slug,
        "seo_description": "این یک متن تستی است",
        "seo_og_image": "http://127.0.0.1:8000/dsb-media/report1401ogimages/download_CE6dcL9.jpeg",
        "bg_image_desktop": "http://127.0.0.1:8000/dsb-media/report1401chapterintrobg/download_QzmoIt8.jpeg",
        "bg_image_mobile": "http://127.0.0.1:8000/dsb-media/report1401chapterintrobg/download_6PVcPBx.jpeg",
        "bg_image_desktop_blur_base64": "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",
        "bg_image_mobile_blur_base64": "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",
        "is_published": True,
        "sections": [
            {
                "id": 2,
                "title": "بخش اول",
                "bg_color_code": None,
                "bg_image_desktop": None,
                "bg_image_mobile": None,
                "bg_image_desktop_blur_base64": None,
                "bg_image_mobile_blur_base64": None,
                "order_for_chapter": 1,
                "is_published": True,
                "widgets": [
                    {
                        "type": "section_added_components_widgets",
                        "order": 1,
                        "component_code": "۵۲۸"
                    },
                    {
                        "type": "section_added_components_widgets",
                        "order": 2,
                        "component_code": "۵۲۷"
                    },
                    {
                        "type": "section_paragraph_widgets",
                        "order": 1,
                        "content": "این بک متن آزمایشی است"
                    },
                    {
                        "type": "section_video_widgets",
                        "order": 0,
                        "url": "https://google.com/video.mp4"
                    }
                ]
            },
            {
                "id": 1,
                "title": "بخش دوم",
                "bg_color_code": None,
                "bg_image_desktop": "/dsb-media/report1401sectionsbg/img_avatar.png",
                "bg_image_mobile": "/dsb-media/report1401sectionsbg/img_avatar_hzmrYUI.png",
                "bg_image_desktop_blur_base64": None,
                "bg_image_mobile_blur_base64": None,
                "order_for_chapter": 2,
                "is_published": True,
                "widgets": [
                    {
                        "type": "section_image_widgets",
                        "order": 1,
                        "alt": "تصویر آزمایشی",
                        "image_desktop": "/dsb-media/report1401imagewidgets/img_avatar.png",
                        "image_mobile": "/dsb-media/report1401imagewidgets/img_avatar_vZXeM18.png",
                        "image_desktop_blur_base64": None,
                        "image_mobile_blur_base64": None
                    },
                    {
                        "type": "section_paragraph_widgets",
                        "order": 2,
                        "content": "این بک متن آزمایشی است."
                    }
                ]
            }
        ]
    }
