from django.shortcuts import render

posts = [
    {
        "author": "Valentin",
        "title": "His mother had always taught him",
        "content": "His mother had always taught him not to ever think of himself as better than others. He'd tried to live by this motto. He never looked down on those who were less fortunate or who had less money than him. But the stupidity of the group of people he was talking to made him change his mind.",
        "date_posted": "July 04, 2024",
    },
    {
        "author": "Valentin",
        "title": "He was an expert but not in a discipline",
        "content": "He was an expert but not in a discipline that anyone could fully appreciate. He knew how to hold the cone just right so that the soft server ice-cream fell into it at the precise angle to form a perfect cone each and every time. It had taken years to perfect and he could now do it without even putting any thought behind it.",
        "date_posted": "July 05, 2024",
    },
    {
        "author": "Valentin",
        "title": "Dave watched as the forest burned up on the hill.",
        "content": "Dave watched as the forest burned up on the hill, only a few miles from her house. The car had been hastily packed and Marta was inside trying to round up the last of the pets. Dave went through his mental list of the most important papers and documents that they couldn't leave behind. He scolded himself for not having prepared these better in advance and hoped that he had remembered everything that was needed. He continued to wait for Marta to appear with the pets, but she still was nowhere to be seen.",
        "date_posted": "July 06, 2024",
    },
    {
        "author": "Valentin",
        "title": "All he wanted was a candy bar.",
        "content": "All he wanted was a candy bar. It didn't seem like a difficult request to comprehend, but the clerk remained frozen and didn't seem to want to honor the request. It might have had something to do with the gun pointed at his face.",
        "date_posted": "July 07, 2024",
    },
    {
        "author": "Valentin",
        "title": "Hopes and dreams were dashed that day.",
        "content": "Hopes and dreams were dashed that day. It should have been expected, but it still came as a shock. The warning signs had been ignored in favor of the possibility, however remote, that it could actually happen. That possibility had grown from hope to an undeniable belief it must be destiny. That was until it wasn't and the hopes and dreams came crashing down.",
        "date_posted": "July 09, 2024",
    },
]


def home(request):
    context = {"posts": posts}
    # The second argument is a string representing the subdirectory inside the
    # templates directory in which our html file lives.
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
