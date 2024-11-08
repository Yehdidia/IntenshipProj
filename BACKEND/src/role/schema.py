class Role(BaseModel):
    id: int
    nom_role: str

class RoleUpdateModel(BaseModel):
    nom_role: str