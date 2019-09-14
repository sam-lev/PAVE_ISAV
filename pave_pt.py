class PAVE
{
public:
    using type = vtkm::Float32;
    using visualisation = vtkm::cont::ArrayHandle<type>
    PAVE(std::string &file);
    void save(std::string &, int, int, visualization &);
};

PAVE paver("variableName");
paver.save(varName, 
           width, 
           height, 
           canvas.GetColorBuffer());