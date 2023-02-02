from django.contrib import admin
from utsab.models import Home, About, Skills, Profile, Category, Portfolio, Footer1, Footer2, Footer3, Contact


admin.site.register(Home)


class ProfileIline(admin.TabularInline):
    model = Profile
    extra = 1
    list_display = ("name", "created_at", "modified_at", )
  
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileIline,
    ]
   
class SkillInline(admin.TabularInline):
    model = Skills
    extra = 2
    list_display = ("name", "created_at", "modified_at", )
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines =[
        SkillInline,
    ]
    list_display = ("name", "created_at", "modified_at", )
    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=("name","email","message")
    


admin.site.register(Portfolio)

admin.site.register(Footer1)



admin.site.register(Footer2)



admin.site.register(Footer3)