from django.conf import settings

def google_analytics(request):

    # DEBUG=Falseの場合に、settings.py内で設定された GOOGLE_ANALYTICS_ID を返す
    ga_tracking_id = getattr(settings, 'GOOGLE_ANALYTICS_ID', False)

    # DEBUG=FalseかつGoogleアナリティクスのトラッキングIDを取得できたら、
    # テンプレート内で'GOOGLE_ANALYTICS_TRACKING_ID'という変数を利用できるようにする
    if not settings.DEBUG and ga_tracking_id:
    #if ga_tracking_id:
        return {
            'GOOGLE_ANALYTICS_ID': ga_tracking_id,
        }
    return {}
