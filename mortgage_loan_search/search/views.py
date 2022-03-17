from django.views import generic


class IndexView(generic.ListView):
    template_name = "search/index.html"
    context_object_name = "search_result_loans"

    def get_queryset(self):
        # ここからスタブ
        search_result_loans = [
            {
                "name": "住宅ローン 全期間引下げプラン",
                "url": "https://www.jibunbank.co.jp/products/homeloan/interest/whole_period/",
                "interest_rate": 0.389,
                "borrowing_age": 45,
                "payoff_age": 80,
            }
        ]
        # ここまでスタブ
        return search_result_loans
