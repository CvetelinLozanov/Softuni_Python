def draw_figures(n):
    if n == 0:
        return

    print('*' * n)
    draw_figures(n - 1)
    print('#' * n)


n = int(input())
draw_figures(n)