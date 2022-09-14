#from django.shortcuts import render
from django.views import View
import json
from modeloRelacionalBaseDeDatos.models import Empresas, Rol
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

#____________________TABLA EMPRESAS______________________

class EmpresasView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #FUNCION PARA OBTENER EMPRESAS

    def get(self,request,idempresas=""):  #FUNCIÓN PARA BUSCAR EMPRESA INDIVIDUALMENTE MEDIANTE EL ID

        if len(idempresas)>0:
            empresa=list(Empresas.objects.filter(id_empresas=idempresas).values())
            if len(empresa)>0:
                datos={'Empresa':empresa}
            else:
                datos={'mensaje':"No se encontró la empresa."} 
        else:
            empresa=list(Empresas.objects.values()) #Empresas es del modelo Empresas y empresa es una variable nueva 
            if len(empresa)>0:
                datos={"mensaje":empresa}
            else:
                datos={"mensaje":"No se encontraron empresas."}

        return JsonResponse(datos)

    #FUNCION PARA CREAR EMPRESAS

    def post(self,request):
        data=json.loads(request.body)
        empresa=Empresas(id_empresas=data['id_empresas'],nombre=data['nombre'],direccion=data['direccion'],ciudad=data['ciudad'],nit=data['nit'],sector_produc=data['sector_produc'],telefono=data['telefono'],fecha_creacion=data['fecha_creacion'])
        empresa.save()
        datos={'mensaje':'Empresa registrada exitosamente.'}

        return JsonResponse(datos)

    #FUNCION PARA ACTUALIZAR EMPRESAS

    def put(self,request,idempresas): #funcion para actualizar la empresa
        data=json.loads(request.body)
        empresa=list(Empresas.objects.filter(id_empresas=idempresas).values()) #este es el formato lista para la lectura del json
        if len(empresa)>0:
                empre=Empresas.objects.get(id_empresas=idempresas)  #dat es el objeto
                empre.nombre=data["nombre"]
                empre.direccion=data["direccion"]
                empre.ciudad=data["ciudad"]
                empre.nit=data["nit"]
                empre.sector_produc=data["sector_produc"]
                empre.telefono=data["telefono"]
                empre.fecha_creacion=data["fecha_creacion"]
                empre.save()
                mensaje={"mensaje":"Empresa actualizada exitosamente."}
        else:
            mensaje={"mensaje":"No se encontró la empresa."}
            
        return JsonResponse(mensaje)

    #FUNCION PARA ELIMINAR EMPRESAS

    def delete(self,request,idempresas):
        empresa=list(Empresas.objects.filter(id_empresas=idempresas).values())
        if len(empresa)>0:
            Empresas.objects.filter(id_empresas=idempresas).delete()
            mensaje={"mensaje": "Empresa eliminada exitosamente."}
        else:
            mensaje={"mensaje": "No se encontró la empresa."}

        return JsonResponse(mensaje)


#______________________TABLA ROL______________________


class RolView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)

    #FUNCION PARA OBTENER UN ROL
    
    def get(selft,request,Id_rol=""):

        if len(Id_rol)>0:
            rol=list(Rol.object.filter(id_rol=Id_rol).values())
            if len(rol)>0:
                datos={'Rol':rol}

            else:
                datos={'mensaje': "No se encontró el Rol."}
        
        else:
            Roles=list(Rol.objects.values())
            if len(Roles)>0:
                datos={"mensaje":Roles}
            else:
                datos={"mensaje":"No se encontro el Rol."}

        return JsonResponse(datos)


    

            
       

         



        
