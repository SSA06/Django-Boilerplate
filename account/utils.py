from django.shortcuts import reverse, redirect


def redirect_to_nxt(request, redirect_path):
    """
    Redirect to GET.get("next") if it exists.
    Else, redirect to redirect_path.
    """
    nxt = request.GET.get("next", None)
    if nxt is not None:
        return redirect(nxt)
    return redirect(reverse(redirect_path))
