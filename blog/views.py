from django.shortcuts import render
from .models import BlogPost, BlogDetail, NftPost, NftDetail, NftImage
from django.views.generic import ListView, DetailView
from home.models import SwirlInfo


#BLOG PAGE
class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'
    ordering = ['-date_posted']
    paginate_by = 5
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        context['blog'] = BlogPost.objects.all()
        context['infos'] = SwirlInfo.objects.all()
        context['intros'] = BlogDetail.objects.all()
        #context = {
        #    'title': 'Blog',
        #    'homes': HomePost.objects.all(),
        #    'infos': SwirlInfo.objects.all()
        #}
        return context
    
class BlogDetailView(DetailView):
    model = BlogPost
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        context['infos'] = SwirlInfo.objects.all()
        context['intros'] = BlogDetail.objects.all()
        return context


#NFT PAGE
class NftListView(ListView):
    model = NftPost
    template_name = 'blog/nft.html'
    context_object_name = 'nfts'
    ordering = ['date_posted']
    paginate_by = 5
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NFT\'S'
        context['nfts'] = NftPost.objects.all()
        context['nfts_intro'] = NftDetail.objects.all()
        context['infos'] = SwirlInfo.objects.all()
        context['nft_imgs'] = NftImage.objects.all()
        #context['nfts_intro'] = BlogDetails.objects.all()
        #context = {
        #    'title': 'Blog',
        #    'homes': HomePost.objects.all(),
        #    'infos': SwirlInfo.objects.all()
        #}
        return context
    
class NftDetailView(DetailView):
    model = NftPost
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NFT\'s'
        context['infos'] = SwirlInfo.objects.all()
        context['nfts_intro'] = NftDetail.objects.all()
        context['nfts'] = NftPost.objects.all()
        context['nft_imgs'] = NftImage.objects.all()
        return context